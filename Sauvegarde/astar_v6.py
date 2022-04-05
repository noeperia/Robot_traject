from __future__ import print_function 
import matplotlib.pyplot as plt
from Fonctionnelle.Main_v2 import GenerateObstacle
from Points import Points
#from Obstacle import *
 
class AStarGraph(object):
    #Define a class board like grid with two barriers
 
    def __init__(self):
        self.barriers = []
        a = Points(50,50)
        c = Points(150,150)

       # print("1 ################")
        #print(GenerateObstacle(a,c))
        #print("################")
        self.barriers.append(GenerateObstacle(a,c))

        #self.barriers.append([(2,4),(2,5),(2,6),(3,6),(4,6),(5,6),(5,5),(5,4),(5,3),(5,2),(4,2),(3,2), (2, 2), (2,3), (2, 4)]) # base
        #self.barriers.append([(2,2),(2,3),(2,4),(2,5),(2,6),(5,2),(5,3),(5,4),(5,5),(5,6)])

        #self.barriers.append([(2,2),(2,3),(2,4),(2,5),(2,6),(3,6),(4,6),(5,6),(5,5),(5,4),(5,3),(5,2),(4,2),(3,2),(2,2)]) #mettre les points dans l'ordre de la ligne

        #self.barriers.append([2,4,2,5,2,6,3,6,4,6,5,6,5,5,5,4,5,3,5,2,4,2,3,2, 2, 2, 2,3, 2, 4]) # ne fonctionne pas
        
    def heuristic(self, start, goal):
        #Use Chebyshev distance heuristic if we can move one square either
        #adjacent or diagonal
        D = 1
        D2 = 1
        dx = abs(start[0] - goal[0])
        dy = abs(start[1] - goal[1])
        return D * (dx + dy) + (D2 - 2 * D) * min(dx, dy)
 
    def get_vertex_neighbours(self, pos):
        n = []
        #Moves allow link a chess king
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]:
            x2 = pos[0] + dx
            y2 = pos[1] + dy
            if x2 < 0 or x2 > 300 or y2 < 0 or y2 > 200:
                continue
            n.append((x2, y2))
        return n
 
    def move_cost(self, a, b):
        for barrier in self.barriers:
            if b in barrier:
                return 100 #Extremely high cost to enter barrier squares
        return 1 #Normal movement cost

    """
    def generate_obstacle(points_a:Points,points_c:Points):
        liste_obs = []
        #contours
        points_b = Points(points_a.x,points_c.y)
        points_d = Points(points_c.x,points_a.y)
        
        liste_obs.append([(points_a.x,points_a.y),(points_a.x,points_c.y),(points_c.x,points_c.y),(points_c.x,points_a.y)]) # il ne faudra pas oublier de fermer la liste ] (voir parametre astar)
        print(liste_obs)
        contours = str(liste_obs[1:-1])
        #contours.append(liste_obs)
        point=[]
        contours_1 = []
        i = 0
        valeur = points_b.y - points_a.y
        #print(valeur)

        while(i<valeur):
            point = points_a.x, points_a.y+i
            contours.append(point) 
            i = i +1

        lst_str = str(contours)[1:-1] 
        print(lst_str,"LA")
        return lst_str 
    """
def AStarSearch(start, end, graph):
 
    G = {} #Actual movement cost to each position from the start position
    F = {} #Estimated movement cost of start to end going via this position
 
    #Initialize starting values
    G[start] = 0
    F[start] = graph.heuristic(start, end)
 
    closedVertices = set()
    openVertices = set([start])
    cameFrom = {}
 
    while len(openVertices) > 0:
        #Get the vertex in the open list with the lowest F score
        current = None
        currentFscore = None
        for pos in openVertices:
            if current is None or F[pos] < currentFscore:
                currentFscore = F[pos]
                current = pos
 
        #Check if we have reached the goal
        if current == end:
            #Retrace our route backward
            path = [current]
            while current in cameFrom:
                current = cameFrom[current]
                path.append(current)
            path.reverse()
            return path, F[end] #Done!
 
        #Mark the current vertex as closed
        openVertices.remove(current)
        closedVertices.add(current)
 
        #Update scores for vertices near the current position
        for neighbour in graph.get_vertex_neighbours(current):
            if neighbour in closedVertices:
                continue #We have already processed this node exhaustively
            candidateG = G[current] + graph.move_cost(current, neighbour)
 
            if neighbour not in openVertices:
                openVertices.add(neighbour) #Discovered a new vertex
            elif candidateG >= G[neighbour]:
                continue #This G score is worse than previously found
 
            #Adopt this G score
            cameFrom[neighbour] = current
            G[neighbour] = candidateG
            H = graph.heuristic(neighbour, end)
            F[neighbour] = G[neighbour] + H
 
    raise RuntimeError("A* failed to find a solution")

    


if __name__=="__main__":
    graph = AStarGraph()
    result, cost = AStarSearch((10,10), (200,200), graph)
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
        