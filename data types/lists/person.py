class Person():
    def __init__(self, name, age, sex):
        self.age = age
        self.name = name
        self.sex = sex


class Employee(Person):
    def __init__(self, name, age, sex, job, salary):
        super().__init__(name, age, sex)
        self.job = job
        self.salary = salary

    def __str__(self):
        return f" Name: {self.name} Age: {self.age} Sex: {self.sex}"


shubham = Employee('shubham', 18, 'M', 'manager', 10000)
print(shubham)
