from Points import Points
class Obstacle:
    def __init__(self,centre:Points,rayon):
        self.centre = centre
        self.rayon = rayon

    def __init__(self,points:list):
        self.points = points
  
    def generate_obstacle(points_a:Points,points_c:Points):
        liste_obs = []
        #contours
        points_b = Points(points_a.x,points_c.y)
        points_d = Points(points_c.x,points_a.y)
        
        liste_obs.append([(points_a.x,points_a.y),(points_a.x,points_c.y),(points_c.x,points_c.y),(points_c.x,points_a.y)]) # il ne faudra pas oublier de fermer la liste ] (voir parametre astar)

        contours = liste_obs
        #contours.append(liste_obs)
        point=[]
        contours_1 = []
        i = 0
        valeur = points_b.y - points_a.y
        print(valeur)

        while(i<valeur):
            point = points_a.x, points_a.y+i
            contours.append(point) 
            i = i +1


        return contours


class Obstacle_Mobile(Obstacle):
      def __init__(self,position,rayon,deplacement):
        self.position = position
        self.rayon = rayon
        self.deplacement = deplacement

