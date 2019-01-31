import math

import Point


# 圆圈继承自点
class Circle(Point.Point):
    def __init__(self,radius,x=0,y=0):
        super().__init__(x,y)
        self.radius=radius
    def edge_distance_from_origin(self):
        return (abs(self.edge_distance_from_origin()-self.radius))

    #装饰器，property装饰器负责把一个方法当做属性调用
    @property
    def area(self):
        return math.pi*(self.radius**2)


def main():
    circle = Circle(4, 3)
    print(circle.area)


if __name__ == '__main__':
    main()
