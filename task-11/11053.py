from math import log2, ceil
l = 440
ans = []
for n in range(1,10000):
    i = ceil(log2(n))
    I = ceil(i * l / 8)
    if I * 1892412 >= 305726 * 2 ** 10:
        ans += [n]
print(min(ans))