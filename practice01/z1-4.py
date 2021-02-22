import math


def f14(n):
    if n == 0:
        return 4
    elif n == 1:
        return 6
    else:
        return (1/22) * f14(n - 2) - math.sin(f14(n - 2)) - 53