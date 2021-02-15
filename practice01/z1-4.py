import math


def foo(n):
    if n == 0:
        return 4
    elif n == 1:
        return 6
    else:
        return (1/22) * foo(n - 2) - math.sin(foo(n - 2)) - 53


print('%.2e' % foo(5))
print('%.2e' % foo(4))