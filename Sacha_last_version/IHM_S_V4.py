##----- Importation des Modules -----##
from tkinter import *
from tkinter import Canvas
from turtle import circle

liste_valid = []
liste_rect = []
liste_rectxy = []
liste_carr = []
liste_carrxy = []
liste_circ = []
liste_circxy = []
##----- Créations des Fonctions -----##
def choisirformes(event):
    if formeee.get() == 1:
        rect1 = dessin.create_rectangle(event.x+100, event.y+40, event.x-100, event.y-50, fill='black', width=3, outline='red')  
        liste_rect.append(rect1)
        liste_rectxy.append(event.x-100)
        liste_rectxy.append(event.y+40)
        liste_rectxy.append(event.x+100)
        liste_rectxy.append(event.y-50)
        
        Text.set(Text.get() + "\nP1(" + str(liste_rectxy[i.get()]) + ";" + str(liste_rectxy[i.get()+1]) + ") P2(" + str(liste_rectxy[i.get()+2]) + ";" + str(liste_rectxy[i.get()+3]) + ")")
        i.set(i.get()+4)

    elif formeee.get() == 2:
        carr = dessin.create_rectangle(event.x+40, event.y+40, event.x-47, event.y-47, fill='black', width=3, outline='red')
        liste_carr.append(carr)
        liste_carrxy.append(event.x-40)
        liste_carrxy.append(event.y+40)
        liste_carrxy.append(event.x+47)
        liste_carrxy.append(event.y-47)
        
        Text.set(Text.get() + "\nP1(" + str(liste_carrxy[j.get()]) + ";" + str(liste_carrxy[j.get()+1]) + ") P2(" + str(liste_carrxy[j.get()+2]) + ";" + str(liste_carrxy[j.get()+3]) + ")")
        j.set(j.get()+4)
    elif formeee.get() == 3:
        cercle = dessin.create_oval(event.x+40, event.y+40, event.x-47, event.y-47, fill='black', width=3, outline='red')
        liste_circ.append(cercle)
        liste_circxy.append(event.x-40)
        liste_circxy.append(event.y+40)
        liste_circxy.append(event.x+47)
        liste_circxy.append(event.y-47)
        
        Text.set(Text.get() + "\nP1(" + str(liste_circxy[k.get()]) + ";" + str(liste_circxy[k.get()+1]) + ") P2(" + str(liste_circxy[k.get()+2]) + ";" + str(liste_circxy[k.get()+3]) + ")")
        k.set(k.get()+4)

    else:
        formeee.set(0)

def valid():
    liste_valid = [*liste_rectxy, *liste_carrxy, *liste_circxy]


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
dessin2.create_window(200,480,window=e1, height=600, width=350)
#varlist = {var: StringVar() for var in ["Text", "Text2", "Text3"]}
Text = StringVar()

i = IntVar(0)
j = IntVar(0)
k = IntVar(0)
LabelResultat = Label(fen, textvariable = Text ,fg = 'white', bg ="grey", width=35, height=40)
dessin2.create_window(200,480,window=LabelResultat)
Text.set("")
#LabelResultat.grid(row=2,column=1, padx = 5, pady = 5)
#label = Label(fen, text="Mode 1", bg='white',font=("Courrier",20))


##----- Création des boutons -----##
formeee = IntVar()

bouton_rectangle = Button(fen, text='Rectangle', command=rec)
bouton_rectangle = dessin2.create_window(75,90, window = bouton_rectangle)

bouton_carre = Button(fen, text='Carré', command=car)
bouton_carre = dessin2.create_window(170,90, window = bouton_carre)

bouton_rond = Button(fen, text='Rond', command=ro)
bouton_rond = dessin2.create_window(245,90, window = bouton_rond)

bouton_valid = Button(fen, text='Confirmer', command=valid)
bouton_valid = dessin2.create_window(340,90, window = bouton_valid)

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