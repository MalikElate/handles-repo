from tkinter import *
from tkinter import filedialog, ttk

mainApp = Tk()

mainApp.title("Youtube Handle Finder")
mainApp.geometry("750x550") 

header_label = Label(mainApp, text="YouTube OG Handle Finder", font=("Helvetica", 16, "bold"))
header_label.pack(pady=20)

# Har file warning
paragraph_text = "To get started add you must add a har file"
paragraph_label = Label(mainApp, text=paragraph_text, wraplength=400, justify="left")
paragraph_label.pack(padx=1, pady=1) 

# Create a Text widget for the centered list
defaultbg = mainApp.cget('bg')
centered_list_text = Text(mainApp, wrap=WORD, height=10, width=400, font=("Helvetica", 14), highlightthickness=0, bg=defaultbg)
centered_list_text.pack(padx=20, pady=20)

# List of items for the centered list
items = [
    "1. Clone the repository to a local directory",
    "2. Navigate to youtube.com/handle, click 'change/choose handle'",
    "3. Open network inspector in ~~your browser~~ _firefox, for now_ (press 'F12', then click the 'network' tab)",
    "4. Change your username in the input box",
    "5. Right click on the request in network inspector, and select 'save all as HAR'",
    "6. Move the HAR file into your youtube-handles folder"
]

# Insert the centered list into the Text widget
for item in items:
    centered_list_text.insert(END, f"{item}\n")
centered_list_text["state"] = DISABLED

# Center-align the list
centered_list_text.tag_config("center", justify="left")
centered_list_text.tag_add("center", "1.0", "end")


def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    print('Selected:', filename)
# Attach Har File button
Button = Button(mainApp, text="Attach Har File", command=UploadAction)
Button.pack(padx=20, pady=20)

mainApp.mainloop()
