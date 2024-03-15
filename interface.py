import tkinter as tk

class MyCanvas(tk.Canvas):
    def __init__(self, master, w=None, h=None):
        tk.Canvas.__init__(self, master)
        self.configure(width=w, height=h)
        self.configure(bg='yellow')
        self.draw_checkers_board(w, h)

    def draw_checkers_board(self, width, height):
        # Dessine le plateau de jeu de dames avec des cases claires et sombres
        square_size = 100
        for row in range(10):
            for col in range(10):
                x1 = col * square_size
                y1 = row * square_size
                x2 = x1 + square_size
                y2 = y1 + square_size
                color = "white" if (row + col) % 2 == 0 else "black"
                self.create_rectangle(x1, y1, x2, y2, fill=color)


class MyButton(tk.Button):
    def __init__(self, master, text):  # Assurez-vous que l'argument text est présent ici
        self.text = text
        tk.Button.__init__(self, master, text=self.text)
        self.configure(width=20, height=2)
        self.configure(bg='green', fg='white')
        self.configure(font=('Times New Roman', 20, 'italic'))
        self.configure(command=self.fonction)

    def fonction(self):
        print(f'Vous avez appuyé sur le bouton {self.text[1]}.')

            
class MyFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, width=100, height=100)
        self.configure(bg='pink')
        self.create_buttons()  # Appel de la méthode pour créer les boutons

    def create_buttons(self):
        # Création du bouton b1
        self.b1 = MyButton(self, text="Quitter")
        self.b1.grid(row=0, column=0, padx=20, pady=20)

        # Création d'un nouveau bouton
        self.b2 = MyButton(self, text="Pause")
        self.b2.grid(row=1, column=0, padx=20, pady=20)
        
        # Création d'un nouveau bouton
        self.b3 = MyButton(self, text="Recommencer")
        self.b3.grid(row=1, column=0, padx=20, pady=20)


class MyLabel(tk.Label):
    def __init__(self, master, t=None):
        # Initialisation de la classe Label avec un texte optionnel
        tk.Label.__init__(self, master, width=30, height=2)
        # Configuration du texte, couleur de fond, couleur du texte et police
        self.configure(text=t)
        self.configure(bg='red', fg='brown')
        self.configure(font=('Arial', 40))

class MyTk(tk.Tk):
    def __init__(self):
        # Initialisation de la classe Tk
        tk.Tk.__init__(self)
        # Configuration de la couleur de fond de la fenêtre principale
        self.configure(bg='light blue')
        # Configuration de la taille et position de la fenêtre
        ##self.state('normal')
        self.geometry('2048x1440+400+0')
        # Création d'un label pour le titre
        self.title = MyLabel(self, t="Jeu de dâme")
        self.title.grid(row=0, column=0, columnspan=2, padx=20, pady=20)
        # Création d'un cadre contenant des boutons
        self.menu = MyFrame(self)
        self.menu.grid(row=1, column=0, padx=20, pady=20)
        # Création d'un canevas
        self.cnv = MyCanvas(self, w=1000, h=1000)
        self.cnv.grid(row=1, column=1, padx=20, pady=20)
