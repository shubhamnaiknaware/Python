class Human:
    def __init__(self, x, y):
        self.name = x
        self.age = y

    def __str__(self):
        return self.name

    def age20(self):
        return f"age after 20 years {self.age+20}"


student1 = Human("shubham", 22)
print(str(student1))
print(student1.age20())
