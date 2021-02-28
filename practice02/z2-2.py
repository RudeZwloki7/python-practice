def f22(x):
    c = (x & 0x700000) << 9
    a = (x & 0x1ff) << 20
    b = (x & 0xffe00)
    e = (x & 0x1f000000) >> 20
    g = (x & 0x80000000) >> 28
    f = (x & 0x60000000) >> 28
    d = (x & 0x800000) >> 23
    return a + b + c + d + e + f + g


# print(f22(0xb72f33e6))
# print(f22(0xeaf87e0d))

