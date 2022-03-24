from typing_extensions import Self

from Points import Points

class Chemin:
    def _init_(self,liste_Points=[]):
        self.liste_Points = liste_Points

    def add_Points(self,p:Points):
        self.liste_Points.append(p)
    
    def clear_chemin(self):
        self.liste_Points.clear()

    
        