##----- Importation des Modules -----##
from tkinter import *
from astar_v2 import *

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

graph = AStarGraph()
result, cost = AStarSearch((0,0), (1500,1500), graph)
print ("route", result)
print ("cost", cost)
""""
plt.plot([v[0] for v in result], [v[1] for v in result])
for barrier in graph.barriers:
    plt.plot([v[0] for v in barrier], [v[1] for v in barrier])
plt.xlim(-1,8)
plt.ylim(-1,8)
plt.show()
"""
print(type(result)) #liste

i=0
print (len(result))
liste_1D = []
while i < len(result):
    x = result[i][0]
    y = result[i][1]
    print(x,y)
    
    liste_1D.append(x)
    liste_1D.append(y)
    i=i+1

print(len(liste_1D))
for pos in liste_1D:
    print(pos) 


liste_point = liste_1D

dessin.create_line(liste_point,fill='red',width=5)

##----- Programme principal -----##
fen.mainloop()                    # Boucle d'attente des événements