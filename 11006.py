from math import log2,ceil
n = 10 + 1700
i = ceil(log2(n))
l = 252
I = ceil(i * l / 8)
k = 4096
print(I * k / 2 ** 10)