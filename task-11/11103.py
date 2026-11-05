from math import log2, ceil
for l in range(1,10000):
    n = 80
    i = ceil(log2(n))
    I = ceil(l * i / 8)
    if I * 1_234_567 > 24 * 2 ** 20:
        print(l)
        break