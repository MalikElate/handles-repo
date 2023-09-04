from tkinter import *
from gui.db_manager import add_handle, get_unchecked_handles, delete_handle, validate_handle, get_har, get_checked_handles
from gui.handle_search import search
from tkinter import filedialog
import asyncio

class HandleFrame(Frame):
    username_view = True
    def __init__(self, master, borderwidth, relief):
        super().__init__(master)
     
        # add label for username instructions
        self.username_input_label = Label(self, text="Enter the usernames to check separated by commas", font=("Helvetica", 14), anchor="w")
        self.username_input_label.grid(column=0, row=1, pady=10)
    
        # Add handles to list box
        listbox_frame = Frame(self)
        listbox_frame.grid(column=0, row=2)
        
        username_listbox_scrollbar = Scrollbar(listbox_frame, orient=VERTICAL)
        username_listbox = Listbox(listbox_frame, yscrollcommand=username_listbox_scrollbar.set)
        username_listbox.grid(column=0, row=2)
        username_listbox_scrollbar.config(command=username_listbox.yview)
        username_listbox_scrollbar.grid(column=1, row=2, sticky="ns")
        def update_username_listbox():
            userNamesToCheck = get_unchecked_handles()
            for item in userNamesToCheck:
                username_listbox.insert(END, item[0])
        update_username_listbox()
        # username results list box
        userNamesResults = get_checked_handles()
        results_listbox_scrollbar = Scrollbar(listbox_frame, orient=VERTICAL)
        results_listbox = Listbox(listbox_frame, yscrollcommand=results_listbox_scrollbar.set)
        results_listbox_scrollbar.config(command=results_listbox.yview)
        
        for item in userNamesResults:
            results_listbox.insert(END, f"{item[0]} {item[2]}")
        
        for i in range(results_listbox.size()):
            item = results_listbox.get(i)
        # Check if the item contains the word "available"
            if "unavailable" not in item.lower():
                results_listbox.itemconfig(i, {'bg': 'green'})
            
        # Create an Entry widget
        entry = Entry(self)
        entry.focus()
        entry.grid(column=0, row=3, pady=10)

        # add handle to list button 
        button_frame = Frame(self, width=400, height=50, pady=10)
        button_frame.grid(column=0, row=4)
        def AddHandleToList():
            entryValue=entry.get()
            if (validate_handle(entryValue) == True):
                print("valid handle")
            else:
                print("invalid handle")
                return
            add_handle(entryValue)
            username_listbox.insert(END, entryValue)
            entry.delete(0, END)
        self.AddHandleToListButton = Button(button_frame, text="Add", command=AddHandleToList)
        self.AddHandleToListButton.grid(row=0, column=1)
        def AddCSVHandleToList():
            filename = filedialog.askopenfilename()
            usernames = []
            num_names = 0
            with open(filename) as csv_file:
                for row in csv_file:
                    if len(row[:-1]) >= 3:  # don't import usernames less than three chars
                        usernames.append(row[:-1])
                        num_names += 1
            # return usernames
            for username in usernames: 
                add_handle(username)
        self.AddHandleToListButton = Button(button_frame, text="Add from csv", command=AddCSVHandleToList)
        self.AddHandleToListButton.grid(row=0, column=2)
        def DeleteHandleToList():
            handle = username_listbox.get(ANCHOR)
            delete_handle(handle)
            username_listbox.delete(ANCHOR)
        self.DeleteHandleToListHandleToListButton = Button(button_frame, text="Delete", command=DeleteHandleToList)
        self.DeleteHandleToListHandleToListButton.grid(row=0, column=0)
        
        # TODO update the username label text to let users know the search is happening []
        # TODO add scroll bar to list box [] 
        # TODO add tutorial video [] 
        
        button_frame_two = Frame(self, width=300, height=50)
        button_frame_two.grid(column=0, row=5)
        # Search button 
        checkHandlesButtonText = "Check Handles"
        async def SearchForHandles(event):
            event.widget.config(text="Searching...")
            harFilePath = get_har()
            userNamesToCheck = get_unchecked_handles()
            userNamesToCheckArray = [item[0] for item in userNamesToCheck]
            await search(harFilePath, userNamesToCheckArray)
            username_listbox.grid_forget()
            username_listbox_scrollbar.grid_forget()
            update_username_listbox()
            username_listbox.grid(column=0, row=2)
            username_listbox_scrollbar.grid(column=1, row=2, sticky="ns")
        self.CheckHandlesButton = Button(button_frame_two, text=checkHandlesButtonText)
        self.CheckHandlesButton.grid(column=1, row=0, pady=10)     
        self.CheckHandlesButton.bind("<Button-1>", lambda event: asyncio.run(SearchForHandles(event)))
                      
        # view results button
        def ToggleView(event):
            global toggleViewButtonText
            if (HandleFrame.username_view):
                username_listbox.grid_forget()
                username_listbox_scrollbar.grid_forget()
                results_listbox.grid(column=0, row=2)
                results_listbox_scrollbar.grid(column=1, row=2, sticky="ns")
                HandleFrame.username_view = False
                event.widget.config(text="View Handles")
            else:
                username_listbox.grid(column=0, row=2) 
                username_listbox_scrollbar.grid(column=1, row=2, sticky="ns")
                results_listbox.grid_forget() 
                results_listbox_scrollbar.grid_forget()
                HandleFrame.username_view = True
                event.widget.config(text="View Results")
            master.update_idletasks()
        self.ToggleViewButton = Button(button_frame_two, text="View Results")
        self.ToggleViewButton.grid(column=0, row=0, pady=10)
        self.ToggleViewButton.bind("<Button-1>", lambda event: ToggleView(event))