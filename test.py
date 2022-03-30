##----- Importation des Modules -----##
from tkinter import *

##----- Création de la fenêtre -----##
fen = Tk()
fen.title('Tracer dans un canevas')

##----- Création des boutons -----##
bouton_quitter = Button(fen, text='Quitter', command=fen.destroy)
bouton_quitter.grid(row = 1, column = 1, padx = 3, pady = 3, sticky=E)

##----- Création du canevas -----##
dessin = Canvas(fen, width = 1300, height = 900, bg = 'white')
dessin.grid(row = 0, column = 0, columnspan = 2, padx = 3, pady = 3)

##----- Dessiner dans le canevas -----##
# Image 
im = PhotoImage(file = '/home/robot/Bureau/NoeSacha/carte_projet.png', master=fen)
logo1 = dessin.create_image(650, 450, image = im )

##----- Programme principal -----##
fen.mainloop()                    # Boucle d'attente des événements