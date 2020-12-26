# object class and its methods inherited by all classes
class Animal:
    def __init__(self):
        self.age = 10

    def eats(self):
        return "eats"


class Mammal(Animal):
    def walks(self):
        return "walks"


genda = Mammal()

print(isinstance(genda, Mammal))
print(isinstance(genda, Animal))
print(issubclass(Mammal, Animal))

print(isinstance(genda, object))
print(issubclass(Mammal, object))
print(issubclass(Animal, object))
