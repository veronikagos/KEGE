from math import ceil, log2
l = 257
for n in range(1,100000):
    i = ceil(log2(n))
    I = ceil(i * l / 8)
    if I * 295_740 <= 33 * 2 ** 20:
        print(n)