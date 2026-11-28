from math import ceil, log2

x = 1024
y = 960
i = ceil(log2(16_384))
k = 400
print(x * y * i * k / 2 ** 23)