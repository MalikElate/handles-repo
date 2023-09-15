import csv
from haralyzer import HarParser
from json import loads
import os
import pickle
from random import randint
import requests
import time
from gui.db_manager import update_handle
import asyncio
import aiohttp

def get_latest_har(har, log):
	print(latest_har)
	latest_har = har
	print("new latest har after latest_har = har", latest_har)
	if log:
		print(f"using latest HAR file: {latest_har}")
	return latest_har 

def save_results(results, log):
	with open("results.csv", "w", encoding="UTF8", newline="") as f:
		writer = csv.writer(f)
		writer.writerow(("username", "available"))
		writer.writerows(results)
	if log:
		print(f"successfully saved {len(results)} results")


def convert_headers(headers, want_cookies, log):
	# originally compressed, which postman and ff handled automatically
	# caused quite the headache figuring out why it couldn't be decoded
	unwanted_headers = ["Content-Length", "Accept-Encoding"]
	# if not want_cookies:
	# 	if log:
	# 		print("not using cookies from HAR file")
	# 	unwanted_headers.append("Cookie")
	new_headers = {}
	for kvp in headers:
		if kvp["name"] not in unwanted_headers:
			new_headers[kvp["name"]] = kvp["value"]
	return new_headers


def import_request(filename, want_cookies, log):
	# verify that it was a successful one(?)
	har_parser = HarParser.from_file(filename)
	# there should only be one request collected (for one page)
	target_request = har_parser.pages[0].post_requests[0]
	return target_request.url, \
		   convert_headers(target_request.request.headers, want_cookies, log), \
		   loads(target_request.request["postData"]["text"])


def load_session(log):
	try:  # check if we've already saved updated cookies
		with open("session.pickle", "rb") as f:
			session = pickle.load(f)
	except FileNotFoundError:  # otherwise, use those from HAR
		session = requests.session()  # or an existing session
		if log:
			print("no session found")
		return session, False
	if log:
		print("using existing session from previous usage")
	return session, True


def save_session(session, log):
	with open("session.pickle", "wb") as f:
		pickle.dump(session, f)
	if log:
		print("session successfully saved")


def delete_session(log):
	os.remove("session.pickle")
	if log:
		print("session successfully removed")

async def check_get_status(username):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://www.youtube.com/@{username}") as response:
                status = response.status
                if status == 200:
                    print("check_get_status returned a 200 for", username)
                elif status == 404:
                    print("check_get_status returned a 404 for", username)
                return status
    except aiohttp.ClientError as e:
        print(f"Error: {e}")
        return None

async def check_username(session, url, headers, payload, username, mode, log):
	prelimCheck = await check_get_status(username)
	status = 200
	if prelimCheck == 200: 
		print("prelimCheck failed returned a 200 for", username)
		return False, session, status 
	else:
		print("prelimCheck passed returned a 404 for", username, "we are in the else statement")
		payload["handle"] = username  # replace previous username with desired search term
		response = session.post(url, headers=headers, json=payload)
		response_data = loads(response.content)
		status = response.status_code  # for passing additional info to main loop of program
		try:
			if response_data["result"]["channelHandleValidationResultRenderer"]["result"] \
					== "CHANNEL_HANDLE_VALIDATION_RESULT_OK":
				return True, session, status
		except KeyError as err:
			if response.status_code == 401:
				print("logged out—saving and shutting down")
			elif response.status_code == 429:
				print("rate limit! sleeping for", end="")
			else:
				print(f"unknown error #{status}, save this message: {response.content}")
		return False, session, status


async def run_full_search(usernames, log, har, mode):
	latest_har = har
	session, session_existed = load_session(log)
	# if session already existed, we don't collect cookies from HAR
	url, headers, payload = import_request(latest_har, (not session_existed), log)
	results = []
	rate_limit_counter = 0
	countfor1har = 0
	for username in usernames:
		countfor1har = countfor1har + 1
		print("countfor1har", countfor1har)
		random_element = randint(0, 9)  # add randomness to sleep time
		time.sleep(random_element)
		success, session, status = await check_username(session, url, headers, payload, username, mode, log)
		results.append((username, success))
		if log:
			success_string = ""
			if not success:
				success_string = "not "
				update_handle(username, "unavailable")
			if success_string == "" and mode == "normal": 
				print(f"Found one!")
				update_handle(username, "available")
				with open('maybeAvailableHandles.csv', 'a') as file:
					file.write("\n{username}")
			# only print "not" if it fails
			# (tried to use ternary operator in fstring, but it looked gross)
			print(f"the handle '{username}' is {success_string}available")
		if status == 200:
			continue  # business as usual
		elif status == 429:  # rate limit, slowing down
			rate_limit_counter += 1
			# if already limit 10 times (even with delays), exit
			if rate_limit_counter >= 3:
				return results, status
			# sleep for progressively more time (with random element)
			total_time = ((rate_limit_counter + 1) * (60 + random_element))
			print(f" {total_time} seconds...")
			time.sleep(total_time)
		else:  # something went wrong, exit gracefully
			return results, status
	return results, 200

async def search(har, userNameToCheck, mode):
	log = True  # set to true if you want to print program logs
	latest_har = har[0][0]
	# usernames = import_usernames("usernames.csv", log)
	usernames = userNameToCheck
	results, status = await run_full_search(usernames, log, latest_har, mode)
	# save_results(results, log)  # log what we have, regardless of whet§her completed
	if status != 200:  # if something went wrong, search exited early
		if status == 401:  # logged out condition
			# delete_session(log)  # old session is stale, we'll get new one from HAR
			print("time to download a new HAR file!, youtube logged you out, be careful")
			return "time to download a new HAR file!, youtube logged you out, be careful"
		elif status == 429:  # rate limit condition
			print("you've been rate limited three times already! if I were you, I'd take the rest of the day off")
			return "you've been rate limited three times already! if I were you, I'd take the rest of the day off"
		else:  # unknown error condition
			print("unknown error occurred—youtube must've changed their API (please tell me!)")
			return"unknown error occurred—youtube must've changed their API (please tell me!)"
if __name__ == "__main__":
	asyncio.run(search())