##----- Importation des Modules -----##
from tkinter import *
from tkinter import Canvas
from turtle import circle


liste_rect = []
liste_carr = []
liste_circ = []
##----- Créations des Fonctions -----##
def choisirformes(event):
    if formeee.get() == 1:
        rect1 = dessin.create_rectangle(event.x+100, event.y+40, event.x-100, event.y-50, fill='black', width=3, outline='red')  
        liste_rect.append(rect1)
        Text.set(dessin2.coords(liste_rect[0]))
    elif formeee.get() == 2:
        carr = dessin.create_rectangle(event.x+40, event.y+40, event.x-47, event.y-47, fill='black', width=3, outline='red')
        liste_carr.append(carr)
    elif formeee.get() == 3:
        cercle = dessin.create_oval(event.x+40, event.y+40, event.x-47, event.y-47, fill='black', width=3, outline='red')
        liste_circ.append(cercle)
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

e1 = Entry(dessin2)
dessin2.create_window(200,480,window=e1, height=700, width=350)
Text = StringVar()
LabelResultat = Label(fen, textvariable = Text ,fg = 'white', bg ="grey", width=30, height=30)
dessin2.create_window(200,400,window=LabelResultat)
Text.set("Résultat : ")
#LabelResultat.grid(row=2,column=1, padx = 5, pady = 5)



#label = Label(fen, text="Mode 1", bg='white',font=("Courrier",20))


##----- Création des boutons -----##
formeee = IntVar()

bouton_rectangle = Button(fen, text='Rectangle', command=rec)
bouton_rectangle = dessin2.create_window(90,90, window = bouton_rectangle)

bouton_carre = Button(fen, text='Carré', command=car)
bouton_carre = dessin2.create_window(200,90, window = bouton_carre)

bouton_rond = Button(fen, text='Rond', command=ro)
bouton_rond = dessin2.create_window(290,90, window = bouton_rond)

##----- Création du Label -----##
lbl = Label(dessin2, text='',fg='black',bg='black')


##----- Dessiner dans le canevas -----##
# TEXTE
message = Label(fen, text='Souris Temps Réel')
message.grid(row=1, column=0, columnspan=2, padx=0, pady=0, sticky=W+E)

bouton_quitter = Button(fen, text='Quitter', command=fen.destroy)
bouton_quitter.grid(row = 1, column = 1, padx = 3, pady = 3, sticky=E)

# Image 
im = PhotoImage(file = '/home/robot/Bureau/NoeSacha/carte_projet.png', master=fen)
logo1 = dessin.create_image(644, 430, image = im )

#Texte IHM PLACER OBSTACLES
dessin2.create_text(200, 30, text='Placer Obstacles : ', fill='#000000', font='Arial 18')

##----- Programme principal -----##
dessin.bind('<Motion>', afficher) ## DEPLACEMENT SOURIS TEMPS REEL
dessin.bind('<Button-1>',choisirformes) ## CLIQUE SOURIS APRES CHOIX FORME


fen.mainloop()                    # Boucle d'attente des événements