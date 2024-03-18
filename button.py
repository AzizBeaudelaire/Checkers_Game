import tkinter as tk

class MyButton(tk.Button):
    def __init__(self, master, text, command=None):
        self.text = text
        tk.Button.__init__(self, master, text=self.text, command=command)
        self.configure(width=20, height=2)
        self.configure(bg='green', fg='white')
        self.configure(font=('Arial', 20))
