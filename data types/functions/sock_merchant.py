a = int(input())
a = list(map(int, input().split()))
s = 0
for i in set(a):
    s += a .count(i)//2
print(s)
