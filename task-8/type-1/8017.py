from itertools import *

alph = sorted('аклмня')
for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if val[0] == 'к' and val[1] == 'м':
        print(pos, val)
        break