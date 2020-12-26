A = [1, 2, 3]
B = [5, 6, 7]
C = [7, 8, 9]
X = [A]+[B]+[C]
print(X)
for i in zip(X):
    print(i)
