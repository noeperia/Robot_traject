##----- Importation des Modules -----##
#import IHM 
from astar import AStarGraph, AStarSearch
from Points import Points

def GenerateObstacle(points_a:Points,points_c:Points):
    liste_obs = []
    #contours
    points_b = Points(points_a.x,points_c.y)
    points_d = Points(points_c.x,points_a.y)
    
    liste_obs = points_a.x,points_a.y,points_a.x,points_c.y,points_c.x,points_c.y,points_c.x,points_a.y
    return liste_obs

if __name__=="__main__":
    a = Points(15,15)
    b = Points(100,100)

    res = GenerateObstacle(a,b)

    print(res)