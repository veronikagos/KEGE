n = 240000
v = 168 * 2 ** 13
for i in range(1,10000):
    I = n * i
    I_ = I * 28 / 100
    if I_ == v:
        print(i)