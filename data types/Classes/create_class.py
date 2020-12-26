# class blueprint to create objects eg.human
# object is an instance of class


class Point:
    # function has at least one parameter that is self
    def draw(self):
        print("draw function is called")


point = Point()
print(type(point))
print(isinstance(point, Point))
print(isinstance(point, int))
