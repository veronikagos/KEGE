from math import ceil, log2
x = 3840
y = 2160
i = 20
I = x * y * i
x_ = 1280
y_ = 720
k = 120
econom = 2322000 * 2 ** 13
for n in range(1,10000):
    i_ = ceil(log2(n))
    I_ = x_ * y_ * i_
    if (I - I_) * k == econom:
        print(n)