class Flyer:
    def fly(self):
        print("fly")


class Swimmer:
    def swims(self):
        print("swims")


class FlyingFish(Flyer, Swimmer):
    pass


m = FlyingFish()
m.swims()
m.fly()
