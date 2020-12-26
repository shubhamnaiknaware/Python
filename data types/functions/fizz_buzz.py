def fizz_buzz(number):
    by3 = number % 3 == 0
    by5 = number % 3 == 0
    if by3 and by5:
        return "fizzbuzz"
    elif not by3 and by5:
        return "buzz"
    elif by3 and not by5:
        return "fizz"
    return number


print(fizz_buzz(15))
