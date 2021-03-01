def naive_mul(x, y):
    r = 0
    for _ in range(y):
        r = r + x
    return r


def test():
    for x in range(100):
        for y in range(100):
            assert naive_mul(x, y) == x * y


test()
print(naive_mul(10, 15))
