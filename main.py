from mytk import MyTk

if __name__ == '__main__':
    try:
        print("Lancement du jeu...")
        # Création de l'instance de l'application et lancement de la boucle principale
        app = MyTk()
        app.mainloop()
        print("Fermeture du jeu...")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
