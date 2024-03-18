import tkinter as tk
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class MyCanvas(tk.Canvas):
    def __init__(self, master, w=None, h=None, board=None):
        tk.Canvas.__init__(self, master)
        self.configure(width=w, height=h)
        # self.configure(bg='yellow')
        self.board = board
        self.draw_checkers_board(w, h)  # Appel de la méthode pour dessiner le plateau
        self.red_piece_img = tk.PhotoImage(file="images/red.png")
        self.vert_piece_img = tk.PhotoImage(file="images/vert.png")
        #self.draw_pieces()

    def draw_checkers_board(self, width, height):
        dx, dy = 0.016, 0.06
        P = np.arange(-5.0, 5.0, dx)
        Q = np.arange(-5.0, 5.0, dy)
        P, Q = np.meshgrid(P, Q)
        res = np.add.outer(range(10), range(10)) % 2

        fig = Figure(figsize=(width/100, height/100), dpi=100)
        ax = fig.add_subplot(111)
        ax.imshow(res, cmap="binary_r")
        ax.axis('off')  # Masquer les axes

        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    #def draw_pieces(self):
    #    if self.board is not None:
    #        print("Chargement de l'image rouge...")
    #        print("Chargement de l'image verte...")
    #        square_size = min(self.winfo_width(), self.winfo_height()) // 10
    #        for row in range(10):
    #            for col in range(10):
    #                x1 = col * square_size
    #                y1 = row * square_size
    #                x2 = x1 + square_size
    #                y2 = y1 + square_size
    #                if self.board[row][col] == 1:
    #                    print("Dessin de la pièce rouge...")
    #                    self.create_image(x1, y1, anchor='nw', image=self.red_piece_img)
    #                elif self.board[row][col] == 2:
    #                    print("Dessin de la pièce verte...")
    #                    self.create_image(x1, y1, anchor='nw', image=self.vert_piece_img)