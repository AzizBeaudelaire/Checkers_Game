import tkinter as tk

class MyLabel(tk.Label):
    def __init__(self, master, t=None):
        tk.Label.__init__(self, master, width=30, height=2)
        self.configure(text=t)
        self.configure(bg='red', fg='brown')
        self.configure(font=('Arial', 40))
