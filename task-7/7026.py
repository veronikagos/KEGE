from math import ceil,log2
x = 1024
y = 960
n = 8192
i = ceil(log2(n))
k = 160
v = 14_680_064
print(i * x * y * k / v)