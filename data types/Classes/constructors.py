class Point:
    color = "RED"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point is {self.x},{self.y}")


# we can change class level attributes which apply to all objects of that type
Point.color = "yellow"
point1 = Point(3, 4)
# we can change class level attributes
print(Point.color)
# instance level attribute
print(point1.color)
