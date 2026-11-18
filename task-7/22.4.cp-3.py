from math import ceil, log2
x = 640
y = 480
v = 600 * 2**13
for n in range(1,10000):
    i = ceil(log2(n * 64))
    if i * x * y <= v:
        print(n)