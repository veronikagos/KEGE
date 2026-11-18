from math import ceil, log2
l = 10
l_ = 25
dop = 48
for n in range(1,10000):
    i = ceil(log2(n))
    I = ceil(l * i / 8)
    I_ = ceil(l_ * i / 8)
    if (I + I_ + dop) * 1536 <= 120 * 2 **10:
        print(n)