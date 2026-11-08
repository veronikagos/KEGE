from math import log2,ceil
x = 1024
y = 768
n = 4096
i = ceil(log2(n))
v = 1310720
for k in range(1,10000):
    I = x * y * i * k
    if I / v <= 300:
        print(k)