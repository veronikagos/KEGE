from math import ceil, log2

n = 10 + 62
i = ceil(log2(n))
for l in range(1,10000):
    I = ceil(i * l / 8)
    if I * 5_895_222 > 23 * 2 ** 20:
        print(l)
        break