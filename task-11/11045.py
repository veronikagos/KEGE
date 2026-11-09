from math import log2,ceil
l = 105
for n in range(1,10000):
    i = ceil(log2(n))
    I = ceil(i * l / 8)
    if I * 65536 >= 7 * 2 ** 20:
        print(n)
        break