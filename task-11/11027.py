from math import log2,ceil
n = 10 + 52 + 458
i = ceil(log2(n))
for l in range(1,10000):
    I = ceil(l * i / 8)
    if I * 862 <= 276 * 2 ** 10:
        print(l)