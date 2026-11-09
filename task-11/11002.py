from math import log2,ceil
n = 10 + 4090
i = ceil(log2(n))
l = 101
I = ceil(l * i / 8)
k = 2048
print(I * k / 2 ** 10)