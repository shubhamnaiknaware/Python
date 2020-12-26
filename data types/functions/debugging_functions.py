def fact(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(fact(1, 2, 3))
