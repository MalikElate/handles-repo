import tkinter as tk

class WidgetFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label = tk.Label(self, text="This is a widget")
        self.label.pack()

        self.button = tk.Button(self, text="Click Me")
        self.button.pack()