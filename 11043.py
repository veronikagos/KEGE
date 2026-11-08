from math import log2,ceil
n = 10 + 52 + 500
i = ceil(log2(n))
for l in range(1,10000):
    I = ceil(l * i / 8)
    if I * 45877 > 49 * 2 ** 20:
        print(l)
        break