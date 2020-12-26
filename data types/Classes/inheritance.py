class Animal:
    def __init__(self):
        self.age = 10

    def eats(self):
        return "eats"


class Mammal(Animal):
    def walks(self):
        return "walks"


class Fish(Animal):
    def swim(self):
        return "Swims"


genda = Mammal()

print(genda.eats())
print(genda.age)
