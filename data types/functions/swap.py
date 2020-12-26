a, b = 10, 11
b = a+b
a = b-a
b = b-a
print(a, b)

# or using tuples
x, y = 2, 3
x, y = y, x
print(x, y)
