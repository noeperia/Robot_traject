from Points import Points
import math

class Obstacle:

    def __init__(self,points:list):
        self.points = points

""" def IsInObstacle(self,points:list):
        for h in len.points:
            pass"""


class Rond(Obstacle):
    def __init__(self,centre:Points,rayon):
        self.centre = centre
        self.rayon = rayon

    def distance(self,p2):
        return math.sqrt((self.centre.x - p2.x)**2 + (self.centre.y - p2.y)**2)

    def IsInObstacle(self,p2):
        return (self.distance(p2)<=self.rayon)

    def __repr__(self) -> str:
        return "rond(centre={},radius={})".format(self.centre, self.rayon)

class Rectangle(Obstacle):
    def __init__(self,a:Points,b:Points):
        self.a = a
        self.b = b

    def distance(self,p2):
        return 

    def IsInObstacle(self,p2):
        return 

    def __repr__(self) -> str:
        return "Rectangle(A={},B={})".format(self.a, self.b)

class Obstacle_Mobile(Obstacle):
      def __init__(self,position,rayon,deplacement):
        self.position = position
        self.rayon = rayon
        self.deplacement = deplacement