import math
import Point
class Circle(Point.Point):
    def __init__(self,radius,x=0,y=0):
        super().__init__(x,y)
        self.radius=radius
    def edge_distance_from_origin(self):
        return (abs(self.edge_distance_from_origin()-self.radius))
    @property
    def area(self):
        return math.pi*(self.radius**2)

