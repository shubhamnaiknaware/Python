a = {'x': 1, 'y': 2}
b = dict(x=1, y=2)
if b['x'] in b.values():
    print(b['x'])


# using get method with default value
print(b.get('x'))
print(b.get('r'))
# with default value
print(b.get('r', 0))
