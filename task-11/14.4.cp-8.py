from math import ceil,log2
n = 10 + 52 + 972
i = ceil(log2(n))
for l in range(1,10000):
    I = ceil(i * l / 8)
    if I * 2048 > 172 * 2 ** 10:
        print(l)
        break