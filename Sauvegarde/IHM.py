##----- Importation des Modules -----##
from tkinter import *
from turtle import left, right

##----- Création de la fenêtre -----##
fen = Tk()
fen.title('Tracer dans un canevas')

##----- Création des boutons -----##
bouton_quitter = Button(fen, text='Quitter', command=fen.destroy)
bouton_quitter.pack

##----- Création du canevas -----##
dessin = Canvas(fen, width = 1300, height = 850, bg = 'white')
dessin.grid(row = 0, column = 0, columnspan = 2, padx = 3, pady = 3)

##----- Dessiner dans le canevas -----##
# Image 
im = PhotoImage(file = '/home/nono/Documents/Projet/Code/carte_projet.png', master=fen)
logo1 = dessin.create_image(650, 450, image = im )


#-----Tracer du chemin-----##
#Chemin
liste_point = 0,0,500,500

dessin.create_line(liste_point,fill='red',width=5)

##----- Programme principal -----##
fen.mainloop()                    # Boucle d'attente des événements