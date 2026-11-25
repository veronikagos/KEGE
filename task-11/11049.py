from math import ceil, log2

l = 65
for n in range(1,10000):
    i = ceil(log2(n))
    I = ceil(i * l / 8)
    if I * 131_072 < 9 * 2 ** 20:
        print(n)