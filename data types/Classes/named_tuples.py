from collections import namedtuple
student = namedtuple("student", ['English', 'Maths', 'Science'])
p1 = student(10, 20, 30)
p2 = student(20, 10, 30)
print(p1 == p2)
