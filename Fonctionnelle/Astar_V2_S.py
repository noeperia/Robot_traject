from __future__ import print_function
from operator import truediv 
import matplotlib.pyplot as plt

from Obstacle import Obstacle, Rond
from Points import Points
import math
 
class AStarGraph(object):
    #Define a class board like grid with two barriers
 
    def __init__(self):
        self.barriers = []
        #self.barriers.append([(2,4),(2,5),(2,6),(3,6),(4,6),(5,6),(5,5),(5,4),(5,3),(5,2),(4,2),(3,2), (2, 2), (2,3), (2, 4)])
        self.barriers.append(Rond(Points(2,4),3))
        self.barriers.append(Rond(Points(2,5),3))
        self.barriers.append(Rond(Points(150,25+50),30))


    def heuristic(self, start, goal):
        #Use Chebyshev distance heuristic if we can move one square either
        #adjacent or diagonal
        D = 1
        D2 = math.sqrt(2)
        dx = abs(start.x - goal.x)
        dy = abs(start.y - goal.y)
        return D * (dx + dy) + (D2 - 2 * D) * min(dx, dy)*self.move_cost(start,goal)
 
    def get_vertex_neighbours(self, pos):
        n = []
        #Moves allow link a chess king
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]:
            x2 = pos.x + dx
            y2 = pos.y + dy
            if x2 < 0 or x2 > 300 or y2 < 0 or y2 > 200:
                continue
            n.append(Points(x2, y2))
        return n
 
    def move_cost(self, a, b):
        for barrier in self.barriers:
            if barrier.IsInObstacle(b):
                return 10000 #Extremely high cost to enter barrier squares
        return 1 #Normal movement cost
 
def IsIn(Poin,liste):
    for P in liste:
        if P == Poin:
            return True

    return False        

def AStarSearch(start, end, graph):

    G = {} #Actual movement cost to each position from the start position
    F = {} #Estimated movement cost of start to end going via this position
 
    #Initialize starting values
    G[start] = 0
    F[start] = graph.heuristic(start, end)
 
    closedVertices = set()  #  closedList = File()
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
            if IsIn(neighbour,closedVertices): ## toto1
                continue #We have already processed this node exhaustively

            ## toto2
            candidateG = G[current] + graph.move_cost(current, neighbour)
            if IsIn(neighbour,openVertices):
                if candidateG >= G[neighbour]:
                    continue #This G score is worse than previously found"""
                
            #Adopt this G score
            cameFrom[neighbour] = current
            G[neighbour] = candidateG
            H = graph.heuristic(neighbour, end)
            F[neighbour] = G[neighbour] + H
            openVertices.add(neighbour) #Discovered a new vertex
 
    raise RuntimeError("A* failed to find a solution")
 
if __name__=="__main__":
    graph = AStarGraph()

    rapport_x = (1288/(3000))*10
    rapport_y = (880/(2000))*10


    result, cost = AStarSearch(Points(250,150), Points(0,0), graph)
    #print ("route", result)
    print ("cost", cost)
    
    print(graph.barriers)
    plt.plot([v.x for v in result], [v.y for v in result])
    #for barrier in graph.barriers:
    #    plt.plot([v.x for v in barrier], [v.y for v in barrier])

    print(result[0][1])

    plt.xlim(0,300)
    plt.ylim(0,200)
    plt.show()
    
