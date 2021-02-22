import math


def f13(n, m):
    left = 0.
    right = 0.
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            left += math.exp(i) - i
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            right += 5 * math.pow(j, 8) + i + 16
    return left + right
