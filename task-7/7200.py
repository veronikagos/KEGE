from math import log2,ceil
x = 1280
y = 720
k = 69
v = 245760 * 8
for n in range(1,10000):
    i = ceil(log2(n))
    I = x * y * k * i
    if I / v > 270:
        print(n)
        break