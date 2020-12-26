def mean(*args):
    return sum(args) / len(args)


def mean2(**kwargs):
    return kwargs


print(mean(1, 2, 3))
print(mean2(a=1, b=2))
