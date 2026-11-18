from math import ceil, log2
l = 156
n = 10 + 1020
i = ceil(log2(n))
I = ceil(l * i / 8)
k = 7168
print(I * k / 2 ** 10)