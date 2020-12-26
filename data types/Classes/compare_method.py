class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __ge__(self, other):
        return self.x >= other.x and self.y >= other.y


point1 = Point(1, 2)
point2 = Point(1, 2)
# returns false is eq method is not defined as it compares
print(point1 == point2)
# point1 > point2 '>' not supported between instances of 'Point' and 'Point'
# greater than also applies to less than
print(point1 < point2)
print(point1 > point2)
#  similarly __ge__ and __le__ also apply each other
print(point1 >= point2)
print(point1 <= point2)
