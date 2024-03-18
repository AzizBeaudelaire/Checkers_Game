import tkinter as tk

class DifficultyButton(tk.Button):
    def __init__(self, master, text, difficulty, **kwargs):
        # Initialise le bouton avec le texte spécifié et une commande pour gérer le clic
        tk.Button.__init__(self, master, text=text, command=self.select_difficulty, **kwargs)
        self.difficulty = difficulty  # Stocke la difficulté associée à ce bouton

    def select_difficulty(self):
        print(f"Difficulté sélectionnée : {self.difficulty}")
        #Todo : change difficulty + reload game and link into func : setdifficulty

class DifficultyFrame(tk.Frame):
    def __init__(self, master):
        # Initialise le cadre pour contenir les boutons de difficulté
        tk.Frame.__init__(self, master)
        self.create_difficulty_buttons()  # Crée les boutons de difficulté

    def create_difficulty_buttons(self):
        difficulties = ["Facile", "Normal", "Difficile"]
        for i, difficulty in enumerate(difficulties):
            # Crée un bouton pour chaque difficulté et l'ajoute au cadre
            button = DifficultyButton(self, text=difficulty, difficulty=difficulty, font=("Arial", 14), padx=20, pady=10)
            button.grid(row=i, column=0, padx=10, pady=5)  # Positionne le bouton dans la grille
