##----- Importation des Modules -----##
#import IHM 
#from astar_v5 import *
from Points import Points
#import matplotlib.pyplot as plt

def GenerateObstacle(points_a:Points,points_c:Points):
    liste_obs = []
    #contours
    points_b = Points(points_a.x,points_c.y)
    points_d = Points(points_c.x,points_a.y)
    
    #liste_obs.append([(points_a.x,points_a.y),(points_a.x,points_c.y),(points_c.x,points_c.y),(points_c.x,points_a.y)]) # il ne faudra pas oublier de fermer la liste ] (voir parametre astar)

    a = points_a.x,points_a.y
    b = points_a.x,points_c.y
    c= points_c.x,points_c.y
    d=points_c.x,points_a.y
    liste_obs.append(a)
    liste_obs.append(b)
    liste_obs.append(c)
    liste_obs.append(d)

    contours = liste_obs
    print(contours,"CONTOUR")
    #contours.append(liste_obs)
    point=[]
    contours_1 = []
    i = 0
    valeur1 = points_b.y - points_a.y
    print(valeur1)

    while(i<valeur1+1):
        point = points_a.x, points_a.y+i
        contours.append(point) 
        i = i +1

    print("Sortie",contours)
    return contours


"""
if __name__=="__main__":

    graph = AStarGraph()
    result, cost = AStarSearch((0,0), (150,100), graph)
    #print ("route", result)
    print ("cost", cost)
    
    plt.plot([v[0] for v in result], [v[1] for v in result])
    for barrier in graph.barriers:
        plt.plot([v[0] for v in barrier], [v[1] for v in barrier])
    plt.xlim(0,300)
    plt.ylim(0,200)
    plt.show()
    
    #print(type(result)) #liste

    i=0
    #print (len(result))
    liste_1D = []
    while i < len(result):
        x = result[i][0]
        y = result[i][1]
        #print(x,y)
        
        liste_1D.append(x)
        liste_1D.append(y)
        i=i+1
    
    #print(len(liste_1D))
# for pos in liste_1D:
#    print(pos) 
    a = Points(1,1)
    b = Points(10,10)

    res = GenerateObstacle(a,b)

    print(res)
    """