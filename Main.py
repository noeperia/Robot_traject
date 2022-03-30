##----- Importation des Modules -----##
import IHM 
from astar import AStarGraph, AStarSearch

graph = AStarGraph()
result, cost = AStarSearch((0,0), (8,8), graph)
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

