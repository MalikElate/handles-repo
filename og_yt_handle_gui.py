from tkinter import *
from tkinter import filedialog
from handle_search import main
from functools import partial

harFilePath = "init file path"

root = Tk()
root.title("Youtube Handle Finder")
root.geometry("750x550") 
handle_frame = Frame(root)
home_frame = Frame(root)
home_frame.pack(fill='both', expand=1)


#################################### Home frame ####################################
home_header_label = Label(home_frame, text="OG YouTube Handle Finder", font=("Helvetica", 16, "bold"))
home_header_label.pack(pady=20)

def font_config(widget, fontslant, event):
    widget.configure(font=fontslant)
paragraph_text = "To get started add you must add a .har file!"
paragraph_label = Label(home_frame, text=paragraph_text, fg="red", wraplength=400, justify="left", font=("Helvetica", 14, "italic"))
paragraph_label.pack(padx=1, pady=1) 

defaultbg = home_frame.cget('bg')
centered_list_text = Text(home_frame, wrap=WORD, height=10, width=400, font=("Helvetica", 14), highlightthickness=0, bg=defaultbg)
centered_list_text.pack(padx=20, pady=20)

items = [
    "1. Clone the repository to a local directory",
    "2. Navigate to youtube.com/handle, click 'change/choose handle'",
    "3. Open network inspector in the FireFox, only FireFox works. (press 'F12', then click the 'network' tab)",
    "4. Change your username in the input box",
    "5. Right click on the request in network inspector, and select 'save all as HAR'",
    "6. Click 'Attach Har File' and select the HAR file you just saved",
]
for item in items:
    centered_list_text.insert(END, f"{item}\n")
centered_list_text["state"] = DISABLED
centered_list_text.tag_config("center", justify="left")
centered_list_text.tag_add("center", "1.0", "end")

def UploadAction(event=None):
    # harFilePath = filedialog.askopenfilename()
    # validate the har file
    # pass in the har file path to main function 
    # main()
    handle_frame.pack(fill='both', expand=1)
    home_frame.pack_forget()
    
# Attach Har File button
AttachHarFileButton = Button(home_frame, text="Attach Har File", command=UploadAction)
AttachHarFileButton.pack(padx=20, pady=20)

#################################### handle Frame ####################################
home_header_label = Label(handle_frame, text="OG YouTube Handle Finder", font=("Helvetica", 16, "bold"))
home_header_label.pack(pady=20)
# add label for username instructions
username_input_label = Label(handle_frame, text="Enter the usernames to check separated by commas", font=("Helvetica", 14), anchor="w")
username_input_label.pack()

# Add handle to list box
userNamesToCheck = []
username_listbox = Listbox(handle_frame) 
username_listbox.pack(pady=6)
for item in userNamesToCheck:
    username_listbox.insert(END, item)
# down the line: add optional file attach for .csv files

# Create an Entry widget
entry = Entry(handle_frame)
entry.focus() 
entry.pack(padx=0, pady=0)

# add handle to list button 

button_frame = Frame(handle_frame, width=200, height=50)
button_frame.pack()

def AddHandleToList():
    entryValue=entry.get()
    userNamesToCheck.append(entryValue)
    username_listbox.insert(END, entryValue)
    entry.delete(0, END)
AddHandleToListButton = Button(button_frame, text="Add", command=AddHandleToList).place(x=40, relx=.5, rely=.5,anchor= CENTER)

def DeleteHandleToList():
    username_listbox.delete(ANCHOR)
DeleteHandleToListHandleToListButton = Button(button_frame, text="Delete", command=DeleteHandleToList).place(x=-40, relx=.5, rely=.5,anchor= CENTER)

# Search button
# populate list with results, change check handles to stop searching, and update the username label text to let users know the search is happening
def SearchForHandles():
    print("hello")
CheckHandlesButton = Button(handle_frame, text="Check Handles", command=SearchForHandles)
CheckHandlesButton.pack(padx=20, pady=20)

# add button to attach new har file, if needed 
# down the line let users know that timeout is happening, add file name of attached har

######################################### fin #########################################
root.mainloop()
if __name__ == "__main__":
    main() 