##----- Importation des Modules -----##
from tkinter import *
from tkinter import Canvas
from turtle import circle
from webbrowser import get
from Points import Points
import math
import time,threading

liste_valid = [] # AFFICHAGE
liste_rect = []
liste_rectxy = [] # AFFICHAGE
liste_carr = []
liste_carrxy = [] # AFFICHAGE
liste_circ = []
liste_circxy = [] # AFFICHAGE
liste_mob = []
liste_cercle = [] # CONTIENT CENTRE + RAYON
liste_ca = [] # CONTIENT P1 et P2 CARRE + RECTANGLE
##----- Créations des Fonctions -----##
def foo():
    print(time.ctime())
    threading.Timer(2,foo).start()
    if started:
        w,x,s,l = dessin.coords('area')
        print(w+47,x+47)
        liste_mob[p.get()-2] = Points(w+47,x+47)
        liste_mob[p.get()-1] = math.sqrt((w-s)**2+(x-l)**2)
    print(liste_ca)
    print(liste_cercle)


def deplacerforme(event):
    global object_id
    if object_id is not None:
        if formeee.get() == 1:
            dessin.coords(object_id, event.x-100, event.y+40, event.x+100, event.y-40)
            liste_rectxy[i.get()-4] = event.x-100
            liste_rectxy[i.get()-3] = event.y+40
            liste_rectxy[i.get()-2] = event.x+100
            liste_rectxy[i.get()-1] = event.y-50
            liste_ca[f.get()-2] = Points(event.x-100,event.y+40)
            liste_ca[f.get()-1] = Points(event.x+100,event.y-50)
        elif formeee.get() == 2:
            dessin.coords(object_id, event.x-40, event.y+40, event.x+47, event.y-47)
            liste_carrxy[j.get()-4] = event.x-40
            liste_carrxy[j.get()-3] = event.y+40
            liste_carrxy[j.get()-2] = event.x+47
            liste_carrxy[j.get()-1] = event.y-47
            liste_ca[f.get()-2] = Points(event.x-40,event.y+40)
            liste_ca[f.get()-1] = Points(event.x+47,event.y-47)
        elif formeee.get() == 3:
            dessin.coords(object_id, event.x-40, event.y+40, event.x+47, event.y-47)
            liste_circxy[k.get()-4] = event.x-40
            liste_circxy[k.get()-3] = event.y+40
            liste_circxy[k.get()-2] = event.x+47
            liste_circxy[k.get()-1] = event.y-47
            ray = math.sqrt((event.x-(event.x-40))**2+(event.y-(event.y+40))**2)
            liste_cercle[o.get()-2] = Points(event.x-40,event.y+40)
            liste_cercle[o.get()-1] = ray
    liste_valid = [*liste_rectxy, *liste_carrxy, *liste_circxy]
    Text.set("")
    for q in range(0,len(liste_valid),4):
        Text.set(Text.get() + "\nP1(" + str(liste_valid[q]) + ";" + str(liste_valid[q+1]) + ") P2(" + str(liste_valid[q+2]) + ";" + str(liste_valid[q+3]) + ")")


def choisirformes(event):
    global debut
    global started
    global fin
    global object_id
    if formeee.get() == 1:
        object_id = dessin.create_rectangle(event.x+100, event.y+40, event.x-100, event.y-50, fill='black', width=3, outline='red')  
        liste_rect.append(object_id)
        liste_rectxy.append(event.x-100)
        liste_rectxy.append(event.y+40)
        liste_rectxy.append(event.x+100)
        liste_rectxy.append(event.y-50)
        liste_ca.append(Points(event.x-100,event.y+40))
        liste_ca.append(Points(event.x+100,event.y-50))
        Text.set(Text.get() + "\nP1(" + str(liste_rectxy[i.get()]) + ";" + str(liste_rectxy[i.get()+1]) + ") P2(" + str(liste_rectxy[i.get()+2]) + ";" + str(liste_rectxy[i.get()+3]) + ")")
        i.set(i.get()+4)
        f.set(f.get()+2)

    elif formeee.get() == 2:
        object_id = dessin.create_rectangle(event.x+40, event.y+40, event.x-47, event.y-47, fill='black', width=3, outline='red')
        liste_carr.append(object_id)
        liste_carrxy.append(event.x-40)
        liste_carrxy.append(event.y+40)
        liste_carrxy.append(event.x+47)
        liste_carrxy.append(event.y-47)
        liste_ca.append(Points(event.x-40,event.y+40))
        liste_ca.append(Points(event.x+47,event.y-47))
        Text.set(Text.get() + "\nP1(" + str(liste_carrxy[j.get()]) + ";" + str(liste_carrxy[j.get()+1]) + ") P2(" + str(liste_carrxy[j.get()+2]) + ";" + str(liste_carrxy[j.get()+3]) + ")")
        j.set(j.get()+4)
        f.set(f.get()+2)

    elif formeee.get() == 3:
        object_id = dessin.create_oval(event.x+40, event.y+40, event.x-47, event.y-47, fill='black', width=3, outline='red')
        liste_circ.append(object_id)
        rayon = math.sqrt((event.x-(event.x-40))**2+(event.y-(event.y+40))**2)
        liste_cercle.append(Points(event.x,event.y))
        liste_cercle.append(rayon)
        print(liste_cercle)
        liste_circxy.append(event.x-40)
        liste_circxy.append(event.y+40)
        liste_circxy.append(event.x+47)
        liste_circxy.append(event.y-47)
        Text.set(Text.get() + "\nP1(" + str(liste_circxy[k.get()]) + ";" + str(liste_circxy[k.get()+1]) + ") P2(" + str(liste_circxy[k.get()+2]) + ";" + str(liste_circxy[k.get()+3]) + ")")
        k.set(k.get()+4)
        o.set(o.get()+2)

    elif formeee.get() == 4:
        debut = event.x
        fin = 1288-debut
        A=(event.x+40,event.y-47)
        B=(event.x-47, event.y+40)
        dessin.create_oval(A, B,outline='red',fill = 'blue',width = 3, tag = 'area')
        #dessin.create_rectangle(event.x+40, event.y+40, event.x-47, event.y-47, fill='blue', width=3, outline='black', tag = 'mobile')
        started = True
        p.set(2)
        animate(1)
    else:
        formeee.set(0)

#http://pascal.ortiz.free.fr/contents/tkinter/tkinter/le_canevas
#http://tkinter.fdex.eu/doc/caw.html#Canvas.tag_bind
#https://sites.google.com/site/pythonpasapas/modules/modules-de-la-bibliotheque-standard/tkinter/tkinterafter
#https://sites.google.com/site/pythonpasapas/modules/modules-de-la-bibliotheque-standard/tkinter/tkinter-canvas-move
# LIEN IMPORTANT :
# https://github.com/arimb/PurePursuit

def valid():
    #liste_valid = [*liste_rectxy, *liste_carrxy, *liste_circxy]
    print("CERCLE : ")
    print(liste_cercle)
    print("CARRES")
    print(liste_ca)

def suppr(event):
    global started
    clic=event.x, event.y
    bord = dessin.find_closest(*clic)
    if formeee.get() == 1:
        del liste_rectxy[i.get()-1]
        del liste_rectxy[i.get()-2]
        del liste_rectxy[i.get()-3]
        del liste_rectxy[i.get()-4]
        i.set(i.get()-4)
        del liste_ca[f.get()-1]
        del liste_ca[f.get()-2]
        f.set(f.get()-2)

    elif formeee.get() == 2:
        del liste_carrxy[j.get()-1]
        del liste_carrxy[j.get()-2]
        del liste_carrxy[j.get()-3]
        del liste_carrxy[j.get()-4]
        j.set(j.get()-4)
        del liste_ca[f.get()-1]
        del liste_ca[f.get()-2]
        f.set(f.get()-2)
    elif formeee.get() == 3:
        del liste_circxy[k.get()-1]
        del liste_circxy[k.get()-2]
        del liste_circxy[k.get()-3]
        del liste_circxy[k.get()-4]
        k.set(k.get()-4)
        del liste_cercle[o.get()-1]
        del liste_cercle[o.get()-2]
        o.set(o.get()-2)
    elif formeee.get() == 4:
        started = False         
    dessin.delete(bord)
    liste_valid = [*liste_rectxy, *liste_carrxy, *liste_circxy]
    Text.set("")
    for q in range(0,len(liste_valid),4):
        Text.set(Text.get() + "\nP1(" + str(liste_valid[q]) + ";" + str(liste_valid[q+1]) + ") P2(" + str(liste_valid[q+2]) + ";" + str(liste_valid[q+3]) + ")")


def horizonta():
    formeee.set(4) # MOBILE HORIZONTAL


def animate(v):
    global debut
    global fin
    #tampon = Text.get()
    if started:
        a,b,c,d=dessin.coords("area")
        if a< debut-100 or c> fin:
            v=-v
        #dessin.move("mobile", v, 0)
        dessin.move("area",v,0)
        #liste_mob=dessin.coords("mobile")
        #liste_mob=dessin.coords("mobile")
        #Text.set(tampon + "\nP1(" + str(liste_mob[0]) + ";" + str(liste_mob[1]) + ") P2(" + str(liste_mob[2]) + ";" + str(liste_mob[3]) + ")")
        dessin.after(50, animate, v)
        

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
object_id = None
debut = None
fin = None
fen = Tk()
fen.title('Tracer dans un canevas')

##----- Création du canevas -----##
dessin = Canvas(fen, width = 1288, height = 859, bg = 'white')
dessin.grid(row = 0, column = 0, columnspan = 2, padx = 3, pady = 3)
dessin2 = Canvas(fen, width = 400, height = 858, bg = 'white')
dessin2.grid(row = 0, column = 40, columnspan = 1, padx = 3, pady = 3)

e1 = Entry(dessin2)
dessin2.create_window(200,480,window=e1, height=600, width=350)
Text = StringVar()

i = IntVar(0)
j = IntVar(0)
k = IntVar(0)
p = IntVar(0)
f = IntVar(0) # VARIABLE CARRE + RECTANGLE
o = IntVar(0) # VARIABLE CERCLE
LabelResultat = Label(fen, textvariable = Text ,fg = 'white', bg ="grey", width=35, height=40)
dessin2.create_window(200,490,window=LabelResultat)
Text.set("")

##----- Création des boutons -----##
formeee = IntVar()

bouton_rectangle = Button(fen, text='Rectangle', command=rec)
bouton_rectangle = dessin2.create_window(75,105, window = bouton_rectangle)

bouton_carre = Button(fen, text='Carré', command=car)
bouton_carre = dessin2.create_window(170,105, window = bouton_carre)

bouton_rond = Button(fen, text='Rond', command=ro)
bouton_rond = dessin2.create_window(245,105, window = bouton_rond)

bouton_valid = Button(fen, text='Confirmer', command=valid)
bouton_valid = dessin2.create_window(340,105, window = bouton_valid)

bouton_hor = Button(fen, text='Horizontal', command=horizonta)
bouton_hor = dessin2.create_window(200,70, window = bouton_hor)


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
dessin.bind('<Button-3>', deplacerforme)
dessin.bind("<Button-2>",suppr)

started = False
# bind tag 

foo()
fen.mainloop()                    # Boucle d'attente des événements