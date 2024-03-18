import tkinter as tk
from button import MyButton
import subprocess


class MyFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, width=100, height=100)
        self.configure(bg='pink')
        self.create_buttons()

    def create_buttons(self):
        # Création du bouton "Quitter" avec la fonction pour fermer la fenêtre
        self.b1 = MyButton(self, text="Quitter", command=self.quit_application)
        self.b1.grid(row=0, column=0, padx=20, pady=20)

        # Création du bouton "Recommencer" avec la fonction pour redémarrer l'application
        self.b2 = MyButton(self, text="Recommencer", command=self.restart_application)
        self.b2.grid(row=1, column=0, padx=20, pady=20)

    def quit_application(self):
        self.master.destroy()

    def restart_application(self):
        self.master.destroy()
        subprocess.run(["clear"])
        print("Redémarrage de l'application ...")
        subprocess.run(["python", "main.py"])