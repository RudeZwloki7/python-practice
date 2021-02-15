import math as m


def foo(x, y):
    return '%.2e' % (m.exp(m.cos(x) - m.log(x)) - 76 * x - (m.tan(m.pow(x, 3)) + m.exp(x)) / (
            37 * m.pow(y, 7) - m.log(x)) - m.sqrt(18 * m.pow(y, 8) + 40 * m.pow(x, 3)))


print(foo(37, 49))
print(foo(51, -66))
