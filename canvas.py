import tkinter as tk
import numpy as np
from PIL import Image, ImageTk 
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class MyCanvas(tk.Canvas):
    def __init__(self, master, w=None, h=None, board=None):
        tk.Canvas.__init__(self, master)  # Appel du constructeur de la classe parente (tk.Canvas)
        self.configure(width=w, height=h)  # Configuration de la taille du canevas
        #self.board = board
        self.board = np.zeros((10, 10), dtype=int)  # Création d'un tableau 2D de dimensions 10x10 rempli de zéros
        self.draw_checkers_board(w, h)
        self.after(10, self.draw_pieces(w,h))  # Utilisation after() pour exécuter draw_pieces() après que le canevas ait été rendu
        
    def draw_checkers_board(self, width, height):
        dx, dy = 0.016, 0.06  # Définition des pas de la grille
        P = np.arange(-5.0, 5.0, dx)  # Création d'une séquence de valeurs pour l'axe des abscisses
        Q = np.arange(-5.0, 5.0, dy)  # Création d'une séquence de valeurs pour l'axe des ordonnées
        P, Q = np.meshgrid(P, Q)  # Création d'une grille de coordonnées
        res = np.add.outer(range(10), range(10)) % 2  # Création d'un motif alternant de cases claires et sombres
        
        fig = Figure(figsize=(width/100, height/100), dpi=100)  # Création d'une figure matplotlib
        ax = fig.add_subplot(111)  # Ajout d'un subplot à la figure
        ax.imshow(res, cmap="binary_r")  # Affichage du motif sur le subplot
        ax.axis('on')  # affichage des axes du graphique
        
        canvas = FigureCanvasTkAgg(fig, master=self)  # Création d'un canevas pour intégrer la figure matplotlib
        canvas.draw()  # Dessin de la figure sur le canevas
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)  # Placement du canevas dans la fenêtre Tkinter
    
    def draw_pieces(self, width, height):
        square_size = min(width, height) // 10  # Utilisation de width et height directement pour calculer la taille des cases
        for row in range(10):
            for col in range(10):
                x1 = col * square_size
                y1 = row * square_size
                x2 = x1 + square_size
                y2 = y1 + square_size

                # Vérifie si la taille de la case est valide
                print(x1, y1)
                if square_size > 0:
                    if (row + col) % 2 == 0:
                        self.create_oval(x1, y1, x2, y2, fill="red")
                    else:
                        self.create_oval(x1, y1, x2, y2, fill="green")

    def jouer_coup(self, event):
        # Récupérer les coordonnées du clic
        x = event.x
        y = event.y
        
        # Déterminer la taille d'une case
        square_size = min(self.winfo_width(), self.winfo_height()) // 10
        
        # Calculer les indices de la case cliquée
        row = y // square_size
        col = x // square_size
        
        # Vérifier si la case est valide
        if 0 <= row < 10 and 0 <= col < 10:
            # Vérifier si la case sélectionnée contient un pion blanc
            if self.board[row][col] == 1:
                # Déplacer le pion blanc en diagonale vers le haut à droite (si possible)
                if row > 0 and col < 9 and self.board[row-1][col+1] == 0:
                    # Mettre à jour les coordonnées du pion
                    self.board[row][col] = 0
                    self.board[row-1][col+1] = 1
                    # Redessiner les pièces sur le plateau
                    self.draw_pieces()
                # Déplacer le pion blanc en diagonale vers le haut à gauche (si possible)
                elif row > 0 and col > 0 and self.board[row-1][col-1] == 0:
                    # Mettre à jour les coordonnées du pion
                    self.board[row][col] = 0
                    self.board[row-1][col-1] = 1
                    # Redessiner les pièces sur le plateau
                    self.draw_pieces()
    