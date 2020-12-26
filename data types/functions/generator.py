from sys import getsizeof
# generators are memory efficient and do not store values

# values is a list
values = [x for x in range(1000)]
print("list:", getsizeof(values))
# values is a generator object
values = (x for x in range(1000))
print("gen:", getsizeof(values))
# for another range
values = (x for x in range(1000000))
print("gen:", getsizeof(values))
