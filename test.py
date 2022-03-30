##----- Importation des Modules -----##
from tkinter import *


##----- Créations des Fonctions -----##
def choisirformes(event):
    if formeee.get() == 1:
        rect1 = dessin.create_rectangle(event.x, event.y, event.x-100, event.y-50, width=2, outline='#d05e82')
    elif formeee.get() == 2:
        carr = dessin.create_rectangle(event.x, event.y, event.x-47, event.y-47, width=2, outline='#d05e82')
    elif formeee.get() == 3:
        cercle = dessin.create_oval(event.x, event.y, event.x-47, event.y-47, fill='orange', outline='blue')
    else:
        formeee.set(0)



def rec():
    formeee.set(1) # RECTANGLE


def car():
    formeee.set(2) # CARRE


def ro():
    formeee.set(3) # CERCLE


def afficher(event): ##AFFICHE COORDONNEES SOURIS TEMPS REEL
    """ Entrées : Un événement de la souris
        Sortie : Affiche en temps réel les coordonnées de la souris dans la zone de texte"""
    abscisse = event.x
    ordonnee = event.y
    message.configure(text="X = {} et Y = {}".format(abscisse, ordonnee))

##----- Création de la fenêtre -----##
fen = Tk()
fen.title('Tracer dans un canevas')

##----- Création du canevas -----##
dessin = Canvas(fen, width = 1288, height = 859, bg = 'white')
dessin.grid(row = 0, column = 0, columnspan = 2, padx = 3, pady = 3)
dessin2 = Canvas(fen, width = 400, height = 858, bg = 'white')
dessin2.grid(row = 0, column = 40, columnspan = 1, padx = 3, pady = 3)


##----- Création des boutons -----##
formeee = IntVar()

bouton_quitter = Button(fen, text='Quitter', command=fen.destroy)
bouton_quitter.grid(row = 1, column = 1, padx = 3, pady = 3, sticky=E)

bouton_rectangle = Button(fen, text='Rectangle', command=rec)
bouton_rectangle = dessin2.create_window(100,150, window = bouton_rectangle)

bouton_carre = Button(fen, text='Carré', command=car)
bouton_carre = dessin2.create_window(100,250, window = bouton_carre)

bouton_rond = Button(fen, text='Rond', command=ro)
bouton_rond = dessin2.create_window(100,320, window = bouton_rond)

##----- Dessiner dans le canevas -----##
# TEXTE
message = Label(fen, text='Ici du texte.')
message.grid(row=8, column=0, columnspan=2, padx=3, pady=3, sticky=W+E)

# Image 
im = PhotoImage(file = '/home/robot/Bureau/NoeSacha/carte_projet.png', master=fen)
logo1 = dessin.create_image(644, 430, image = im )

#Texte IHM PLACER OBSTACLES
dessin2.create_text(200, 30, text='Placer Obstacles : ', fill='#000000', font='Arial 18')

##----- Programme principal -----##
dessin.bind('<Motion>', afficher) ## DEPLACEMENT SOURIS TEMPS REEL
dessin.bind('<Button-1>',choisirformes) ## CLIQUE SOURIS APRES CHOIX FORME
fen.mainloop()                    # Boucle d'attente des événements