from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from functools import partial
from gui.home_frame import HomeFrame
from gui.handle_frame import HandleFrame
from gui.db_manager import init_db, get_har, add_har, validate_har

class App(Tk):
    def __init__(self):
        super().__init__()

        self.title("Youtube Handle Finder")
        self.geometry("750x550") 
        self.columnconfigure(0, weight=1)
        self.home_header_label = Label(self, text="OG YouTube Handle Finder", font=("Helvetica", 16, "bold"))
        self.home_header_label.grid(column=0, row=0, pady=20)

        # #start the db
        init_db()
        
        handle_frame = HandleFrame(self, borderwidth=2, relief="solid")
        home_frame = HomeFrame(self, borderwidth=2, relief="solid")
        if get_har() == []:
            home_frame.grid(column=0, row=1)
        else:
            handle_frame.grid(column=0, row=1)
            
        # Attach Har File button
        def UploadAction(event):
            harFilePath = filedialog.askopenfilename()
            if validate_har(harFilePath): 
                add_har(harFilePath)
                handle_frame.grid(column=0, row=1)
                handle_frame.columnconfigure(0, weight=1)
                home_frame.grid_forget()
                event.widget.grid_forget()
            else: 
                messagebox.showerror(title=None, message="Invalid Har File")
        self.AttachHarFileButton = Button(self, text="Attach Har File")
        self.AttachHarFileButton.grid(column=0, row=2)
        self.AttachHarFileButton.bind("<Button-1>", lambda event: UploadAction(event))