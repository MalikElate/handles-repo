from tkinter import *
from gui.db_manager import add_handle, get_unchecked_handles, delete_handle, validate_handle
from gui.handle_search import search

class HandleFrame(Frame):
    username_view = True
    def __init__(self, master, borderwidth, relief):
        super().__init__(master)
     
        # add label for username instructions
        self.username_input_label = Label(self, text="Enter the usernames to check separated by commas", font=("Helvetica", 14), anchor="w")
        self.username_input_label.grid(column=0, row=1)
    
        self.config(borderwidth=borderwidth, relief=relief) 
    
        # # Add handles to list box
        userNamesToCheck = get_unchecked_handles()
        username_listbox = Listbox(self) 
        username_listbox.grid(column=0, row=2,pady=10)
        for item in userNamesToCheck:
            username_listbox.insert(END, item[0])
            
        userNamesResults = ["deez", "nuts", "gottem"]
        results_listbox = Listbox(self) 
        for item in userNamesResults:
            results_listbox.insert(END, item)
            
        # # Create an Entry widget
        entry = Entry(self)
        entry.focus()
        entry.grid(column=0, row=3)

        # # add handle to list button 
        button_frame = Frame(self, width=200, height=50)
        button_frame.grid(column=0, row=4)
        def AddHandleToList():
            entryValue=entry.get()
            if (validate_handle(entryValue) == True):
                print("valid handle")
            else:
                print("invalid handle")
                return
            add_handle(entryValue)
            userNamesToCheck.append(entryValue)
            username_listbox.insert(END, entryValue)
            entry.delete(0, END)
        self.AddHandleToListButton = Button(button_frame, text="Add", command=AddHandleToList).place(x=40, relx=.5, rely=.5,anchor= CENTER)

        def DeleteHandleToList():
            handle = username_listbox.get(ANCHOR)
            delete_handle(handle)
            username_listbox.delete(ANCHOR)
        self.DeleteHandleToListHandleToListButton = Button(button_frame, text="Delete", command=DeleteHandleToList).place(x=-40, relx=.5, rely=.5,anchor= CENTER)
        # TODO populate list with results [] 
        # TODO update the username label text to let users know the search is happening []
        # TODO add scroll bar to list box [] 
        # TODO add button to attach new har file, if needed []
        # TODO line let users know that timeout is happening, add file name of attached har []
        button_frame_two = Frame(self, width=300, height=50)
        button_frame_two.grid(column=0, row=5)
        # Search button
        checkHandlesButtonText = "Check Handles"
        def SearchForHandles():
            # search(harFilePath)
            global checkHandlesButtonText
            checkHandlesButtonText = "Stop Searching"
            CheckHandlesButton.config(text=checkHandlesButtonText)
        CheckHandlesButton = Button(button_frame_two, text=checkHandlesButtonText, command=SearchForHandles).place(x=70, relx=.5, rely=.5,anchor= CENTER)

        # # view results button
        def ToggleView():
            if (HandleFrame.username_view):
                username_listbox.grid_forget()
                results_listbox.grid(column=0, row=2)
                HandleFrame.username_view = False
            else:
                username_listbox.grid(column=0, row=2)   
                results_listbox.grid_forget() 
                HandleFrame.username_view = True
            master.update_idletasks()
        toggleViewButtonText = "View Results"
        self.ToggleViewButton = Button(button_frame_two, text=toggleViewButtonText, command=ToggleView).place(x=-70, relx=.5, rely=.5,anchor= CENTER)