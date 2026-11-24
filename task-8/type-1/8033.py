from itertools import *

alph = sorted('январь')
for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    for i in range(4):
        if val[i:i + 2] == 'яя':
            val = '*****'
    if val[0] != 'я' and val.count('ь') <= 1 and val.count('*') == 0:
        print(pos, val)
