l = ['a', 'b', 'c', 'd']
print(l.index('a'))
# l.index('t') gives value error
if 't' in l:
    print(l.index('t'))
else:
    print('t not in l')
print(l.count('b'))
