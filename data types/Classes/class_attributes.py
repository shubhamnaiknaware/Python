import math


class Point:
    color = "Red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point is {self.x},{self.y}")


point1 = Point(3, 4)
point1.z = 5
