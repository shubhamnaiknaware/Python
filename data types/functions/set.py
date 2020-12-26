# indexing not allowed in sets
a = [1, 2, 3, 3, 4, 5, 6, 7, 2, 3, 5, 6]
s1 = set(a)
b = [7, 8, 9, 0]
s2 = set(b)
# union of two sets
print(s1.union(s2))
print(s1 | s2)
# intersection of two sets
print(s1.intersection(s2))
print(s1 & s2)
# difference s1-s2
print(s1.difference(s2))
print(s1-s2)
# symmetric difference
print(s1.symmetric_difference(s2))
print(s1 ^ s2)
