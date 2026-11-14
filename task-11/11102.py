from math import log2, ceil
l = 7
n = 26 + 10
i = ceil(log2(n))
I = ceil(l * i / 8)
dop = 9
print((I + dop) * 30)