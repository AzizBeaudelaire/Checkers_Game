import tkinter as tk
import numpy as np
from frame import MyFrame
from canvas import MyCanvas
from label import MyLabel
from button_difficult import DifficultyFrame  # Importez votre cadre de boutons de difficulté


class MyTk(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.configure(bg='light blue')
        self.geometry('1848x1080+400+0')
        self.title = MyLabel(self, t="Jeu de dames")
        self.title.grid(row=0, column=0, columnspan=2, padx=20, pady=20)
        self.menu = MyFrame(self)
        self.menu.grid(row=1, column=0, padx=20, pady=20)
        self.board = np.zeros((10, 10))  # Plateau de jeu initial vide
        self.cnv = MyCanvas(self, w=800, h=800, board=self.board)
        self.cnv.grid(row=1, column=1, padx=20, pady=20)
        
        self.difficulty_frame = DifficultyFrame(self)
        self.difficulty_frame.grid(row=1, column=2, padx=20, pady=20)  # Placez-le à côté du cadre de menu

