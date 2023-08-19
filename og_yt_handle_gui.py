from tkinter import *
from tkinter import filedialog
from handle_search import search
from functools import partial
from home_frame import WidgetFrame  # Import your custom widget class
from db_manager import init_db

#start the db
init_db(); 

root = Tk()
root.title("Youtube Handle Finder")
root.geometry("750x550") 

# widget_frame = WidgetFrame(root)
# widget_frame.pack()

home_frame = Frame(root, borderwidth=2, relief="solid")
home_frame.pack(expand=True, fill='both')
home_frame.columnconfigure(0, weight=1)
handle_frame = Frame(root, borderwidth=2, relief="solid")

#################################### Home frame ####################0################
harFilePath = "init file path"
home_header_label = Label(home_frame, text="OG YouTube Handle Finder", font=("Helvetica", 16, "bold"))
home_header_label.grid(column=0, row=0)

paragraph_label = Label(home_frame, text="To get started add you must add a .har file!", fg="red", wraplength=400, justify="left", font=("Helvetica", 14, "italic"))
paragraph_label.grid(column=0, row=1) 

centered_list_text_text = "1. Clone the repository to a local directory\n2. Navigate to youtube.com/handle, click 'change/choose handle'\n3. Open network inspector in the FireFox, only FireFox works. (press 'F12', then click the 'network' tab)\n 4. Change your username in the input box\n5. Right click on the request in network inspector, and select 'save all as HAR'\n6. Click 'Attach Har File' and select the HAR file you just saved"
centered_list_text = Label(home_frame, text=centered_list_text_text, justify="left", font=("Helvetica", 14))
centered_list_text.grid(column=0, row=2)

# Attach Har File button
def UploadAction():
    handle_frame.pack(fill='both', expand=1)
    home_frame.pack_forget()
    handle_frame.columnconfigure(0, weight=1)
AttachHarFileButton = Button(home_frame, text="Attach Har File", command=UploadAction)
AttachHarFileButton.grid(column=0, row=3)

#################################### handle Frame ####################################
home_header_label = Label(handle_frame, text="OG YouTube Handle Finder", font=("Helvetica", 16, "bold"))
home_header_label.grid(column=0, row=0)
# add label for username instructions
username_input_label = Label(handle_frame, text="Enter the usernames to check separated by commas", font=("Helvetica", 14), anchor="w")
username_input_label.grid(column=0, row=1)

# Add handle to list box
userNamesToCheck = []
username_listbox = Listbox(handle_frame) 
username_listbox.grid(column=0, row=2)
for item in userNamesToCheck:
    username_listbox.insert(END, item)
    
userNamesResults = ["deez", "nuts", "gottem"]
results_listbox = Listbox(handle_frame) 
for item in userNamesResults:
    results_listbox.insert(END, item)
    
# Create an Entry widget
entry = Entry(handle_frame)
entry.focus() 
entry.grid(column=0, row=3)

# add handle to list button 
button_frame = Frame(handle_frame, width=200, height=50)
button_frame.grid(column=0, row=4)
def AddHandleToList():
    entryValue=entry.get()
    userNamesToCheck.append(entryValue)
    username_listbox.insert(END, entryValue)
    entry.delete(0, END)
AddHandleToListButton = Button(button_frame, text="Add", command=AddHandleToList).place(x=40, relx=.5, rely=.5,anchor= CENTER)

def DeleteHandleToList():
    username_listbox.delete(ANCHOR)
DeleteHandleToListHandleToListButton = Button(button_frame, text="Delete", command=DeleteHandleToList).place(x=-40, relx=.5, rely=.5,anchor= CENTER)

# TODO add button to switch between search and result [x]
# TODO change check handles to stop searching [x]
# TODO add db for the usernames []
# TODO populate list with results [] 
# TODO and update the username label text to let users know the search is happening []
# TODO add scroll bar to list box [] 
# TODO refactor frames to separate files []
button_frame_two = Frame(handle_frame, width=300, height=50)
button_frame_two.grid(column=0, row=5)
# Search button
checkHandlesButtonText = "Check Handles"
def SearchForHandles():
    if harFilePath != "init file path":
        main(harFilePath)
        global checkHandlesButtonText
        checkHandlesButtonText = "Stop Searching"
        CheckHandlesButton.config(text=checkHandlesButtonText)
CheckHandlesButton = Button(button_frame_two, text=checkHandlesButtonText, command=SearchForHandles).place(x=70, relx=.5, rely=.5,anchor= CENTER)

#view results button]
def ToggleView():
    print("toggle view")
    if username_listbox.winfo_ismapped():
        username_listbox.grid_forget()  # Hide the first label
        results_listbox.grid(column=0, row=2)     # Show the second label
    else:
        username_listbox.grid(column=0, row=2)   
        results_listbox.grid_forget()  # Hide the second label
toggleViewButtonText = "View Results"
ToggleViewButton = Button(button_frame_two, text=toggleViewButtonText, command=ToggleView).place(x=-70, relx=.5, rely=.5,anchor= CENTER)

# TODO add button to attach new har file, if needed 
# down the line let users know that timeout is happening, add file name of attached har

######################################### fin #########################################
root.mainloop()