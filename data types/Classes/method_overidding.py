class Animal:
    def __init__(self):
        self.weight = 10
        print("Animal Constructor")

# super class position can be altered to define
# whch constructor to run first


class Mammal(Animal):
    def __init__(self):
        # super().__init__() here gives Animal Constructor,Mammal Constructor,10
        self.age = 8
        print("Mammal constructor")
        super().__init__()


m = Mammal()
print(m.weight)
