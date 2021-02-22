import math as m


def f12(x):
    if x < 98:
        return m.fabs(m.sin(x)) + 15 * m.pow(x, 6) + 81
    elif 98 <= x < 183:
        return m.cos(73 * m.pow(x, 5)) - m.pow(x, 4)
    elif 183 <= x < 194:
        return m.cos(m.pow(x, 7) - 18 * m.pow(x, 8)) + m.tan(98 * m.pow(x, 8))
    elif x >= 194:
        return m.pow(x, 3) + m.pow(x, 2)