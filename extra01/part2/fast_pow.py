def fast_pow(x, y):
    result = 1
    while y > 0:
        if y == 1:
            return result * x
        if y % 2 == 1:
            result *= x
        y //= 2
        x *= x
    return result


def test():
    for x in range(100):
        for y in range(100):
            assert fast_pow(x, y) == pow(x, y)


test()
print(fast_pow(5, 3))
