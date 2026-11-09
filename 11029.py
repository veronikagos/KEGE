from math import log2,ceil
n = 10 + 26 + 450
i = ceil(log2(n))
for l in range(1,10000):
    I = ceil(i * l / 8)
    if I * 708 > 213 * 2 ** 10:
        print(l)
        break