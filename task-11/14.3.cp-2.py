from math import ceil, log2
l = 2783
for n in range(1,10000):
    i = ceil(log2(n))
    I = ceil(i * l / 8)
    if I * 3845627 >= 11 * 2 ** 30:
        print(n)