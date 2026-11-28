from string import printable
from itertools import product

cnt = 0
for val in product(printable[:7], repeat=5):
    val = ''.join(val)
    if val[0] != '0' and val.count('0') == 1 and val.count('1') <= 2:
        cnt += 1
print(cnt)