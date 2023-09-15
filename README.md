# youtube-handles
_programmatically check availability of youtube handles_
* use your own youtube account, no password required (see disclaimer))
* support for force logout, rate limiting

## Download for all platforms 
* 

## Technologies
* Python 3.10
* [requests](https://github.com/psf/requests) ( for interacting with youtube's API)
* [haralyzer](https://github.com/haralyzer/haralyzer) (for parsing HAR files, to allow dynamic account session imports)
* Tkinter

## Install source code
* [Video Walkthrough](https://youtu.be/7Zqjw5O6wd8)
* Clone the repository to a local directory (or [download](https://github.com/maxtheaxe/youtube-handles/archive/refs/heads/main.zip) it, extract it)
* Open that directory in your terminal (`cd <insert folder path here>`)
* Install the dependencies (`pip install -r requirements.txt`)
* Navigate to [youtube.com/handle](https://www.youtube.com/handle), click 'change/choose handle'
* Open network inspector in ~~your browser~~ _firefox, for now_ (press 'F12', then click the 'network' tab)
* Change your username in the input box
* Right click on the request in network inspector, and select 'save all as HAR'
* Attach a har file from the gui

## Usage
* Run run.py

## Disclaimers & Notes
* I am not responsible if you end up getting your account banned (I recommend using one you don't care about)
* Feel free to submit pull requests
* Fresh Google Accounts won't work
* This project is free and credits to max the axe for publishing the code for using har files and making post requests to youtube's api. Check out his project [here](https://github.com/maxtheaxe/youtube-handles)
* each har file can make about 50 requests 
* This project is freeware
