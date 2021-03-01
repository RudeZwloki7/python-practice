def fast_mul(x, y, result=0):
    if x == 0 or y == 0:
        return 0
    if x == 1:
        return result + y
    if x % 2 == 1:
        result += y

    return fast_mul(x // 2, y * 2, result)


def test():
    for x in range(100):
        for y in range(100):
            assert fast_mul(x, y) == x * y


test()
print(fast_mul(12, 15))
