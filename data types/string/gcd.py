a = [1, 2, 3, 4, 5, 6]
b = [100, 200]
l = [max(a)*i for i in range(1, 1000) if max(a)*i < min(b)]
print(l)
