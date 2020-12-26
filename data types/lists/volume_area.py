from functools import reduce


def mean(l):
    pass


def volume(l):
    the_mean = reduce(lambda x, y: x*y, l)
    print(the_mean)


volume([1, 2, 3])
