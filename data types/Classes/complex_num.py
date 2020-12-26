import math


class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        real = self.real + other.real
        imaginary = self.imaginary + other.imaginary
        print(real, imaginary)
        return Complex(real, imaginary)

    def __sub__(self, other):
        real = self.real-other.real
        imaginary = self.imaginary-other.imaginary
        print(real, imaginary)
        return Complex(real, imaginary)

    def __mul__(self, other):
        real = (self.real*other.real)-(self.imaginary*other.imaginary)
        imaginary = self.real*other.imaginary + self.imaginary*other.real
        print(real, imaginary)
        return Complex(real, imaginary)

    def __truediv__(self, other):
        d = pow(other.real, 2)+pow(other.imaginary, 2)
        real = (self.real*other.real+self.imaginary*other.imaginary) / d
        imaginary = (self.imaginary*other.real - self.real*other.imaginary)/d
        print(real, imaginary)
        return complex(real, imaginary)

    def mod(self):
        real = math.sqrt(self.real**2 + self.imaginary**2)
        return complex(real, 0)

    def __str__(self):
        print(self.imaginary)
        if self.imaginary > 0:
            result = f"{self.real:.2f}+{self.imaginary:.2f}i"
        else:
            result = f"{self.real:.2f}-{abs(self.imaginary):.2f}i"
        return result


if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
