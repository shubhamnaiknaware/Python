l = [[1, 2], [3, 4], [5, 6], [7, 8]]
j = list(map(lambda x: x[1], l))
print(j)
m = [[1, 2], [3, 4], [5, 6], [7, 8]]
k = list(filter(lambda x: x[1] < 10, m))
print(k)
