from tkinter import *

class HomeFrame(Frame):
    def __init__(self, master, borderwidth, relief):
        super().__init__(master)
     
        self.paragraph_label = Label(self, text="To get started add you must add a .har file!", fg="red", wraplength=400, justify="left", font=("Helvetica", 14, "italic"))
        self.paragraph_label.grid(column=0, row=1) 

        centered_list_text_text = "1. Clone the repository to a local directory\n2. Navigate to youtube.com/handle, click 'change/choose handle'\n3. Open network inspector in the FireFox, only FireFox works. (press 'F12', then click the 'network' tab)\n4. Change your username in the input box\n5. Right click on the request in network inspector, and select 'save all as HAR'\n6. Click 'Attach Har File' and select the HAR file you just saved"
        self.centered_list_text = Label(self, text=centered_list_text_text, justify="left", font=("Helvetica", 14))
        self.centered_list_text.grid(column=0, row=2)
        
        self.config(borderwidth=borderwidth, relief=relief) 
