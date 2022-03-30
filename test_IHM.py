from logging import root
from tkinter import * # Import de la bibliotheque tkinter



root = Tk() # Creation de la fenetre principale

root.geometry("2000x1000") #largeur x hauteur

#Mise a l'echelle carte :

hauteur = 858
largeur = 1286

#label
bg = PhotoImage(file="/home/nono/Documents/Projet/Code/carte_projet.png") #Image de fond d'ecran de la carte (background)
#bg = Image.open()
#LABEL 1 (EN HAUT A GAUCHE) : CARTE

#label1 = Label( root, image = bg) 
#label1.place(x = 0, y = 0) 

c1 = Canvas(root, bg = "white", height = 1000, width = 1000,cursor='exchange') #canva choix chemin (echelle 2/5 --> hauteur*0.4 = )




image = c1.create_image(400,800,image=bg)

#CANVAS 2 (EN HAUT A DROITE) : CHEMIN

c2 = Canvas(root, bg = "white", height = 400, width = 560) #canva choix chemin (echelle 2/5 --> hauteur*0.4 = )


liste_point = 10,40,60,90

c2.create_line(liste_point,fill='red',width=5)


#CANVAS 3 (EN BAS A DROITE) : OBSTACLE


c3 = Canvas(root, bg = "blue", height = 658, width = 560) #canva Liste obstacle

liste_obstacle = 'Obs_Fixe_1 : x= .... y=....','Obs_Mobile_1 : x=..... y=....' #Recupérer de l'objet qui contient la liste de tous les obstacles


label = Label( c3, text="Liste obstacle : \n")
label.pack()

label2 = Label( c3, text=liste_obstacle)
label2.pack()

#CANVAS 4 (EN BAS A GAUCHE) : LEGENDE

c4 = Canvas(root, bg = "green", height = 200, width = largeur) #canva Legendes




#
# carte.place(x=0,y=0)
c2.place(x=largeur,y=0)
c3.place(x=largeur,y=400)
c4.place(x=0,y=hauteur)

#coord = 10, 50, 240, 210
#arc = C.create_arc(coord, start = 0, extent = 150, fill = "red")
#line = C.create_line(10,10,200,200,fill = 'white')


#C.pack()

##----- Création des boutons -----##
bouton_quitter = Button(root, text='Quitter', command=root.destroy)
bouton_quitter.pack()


#bouton_quitter.grid(row = 1, column = 1, padx = 3, pady = 3, sticky=E)


root.mainloop()