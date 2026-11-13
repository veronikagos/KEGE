from math import log2, ceil
n = 10 + 26 + 34
i = ceil(log2(n))
for l in range(1,1000):
    I = ceil(i * l / 8)
    if I * 1142 > 305 * 2 ** 10:
        print(l)
        break