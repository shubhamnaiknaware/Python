class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"


point1 = Point(1, 2)
# print(point1) returns <__main__.Point object at 0x03247298>
print(str(point1))
print(point1)
# use str or __str__ to convert object to string
