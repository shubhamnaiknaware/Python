class Box:
    def __init__(self, x, y, z):
        self.length = x
        self.height = y
        self.breadth = z

    def __str__(self):
        return f"({self.length},{self.breadth},{self.height})"

    def __add__(self, other):
        return Box(self.length + other.length, self.height + other.height, self.breadth + other.breadth)

    def __sub__(self, other):
        return Box(self.length - other.length, self.height - other.height, self.breadth - other.breadth)

    def __mul__(self, other):
        return Box(self.length * other.length, self.height * other.height, self.breadth * other.breadth)

    def volume(self):
        return (self.length * self.height * self.breadth)


box1 = Box(5, 6, 7)
box2 = Box(5, 6, 7)
print("the sum of volume of two boxes is")
print(box1.volume() + box2.volume())

# print(box1 + box2) returns box object which gives <__main__.Box object at 0x01697190> without str function
print(box1 + box2)
print(box1 - box2)
print(box1 * box2)
