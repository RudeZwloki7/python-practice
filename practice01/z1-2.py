import math as m


def foo(x):
    if x < 98:
        return '%.2e' % (m.fabs(m.sin(x)) + 15 * m.pow(x, 6) + 81)
    elif 98 <= x < 183:
        return '%.2e' % (m.cos(73 * m.pow(x, 5)) - m.pow(x, 4))
    elif 183 <= x < 194:
        return '%.2e' % (m.cos(m.pow(x, 7) - 18 * m.pow(x, 8)) + m.tan(98 * m.pow(x, 8)))
    elif x >= 194:
        return '%.2e' % (m.pow(x, 3) + m.pow(x, 2))


print(foo(57))
print(foo(108))
