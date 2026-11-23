from itertools import *
alph = sorted('теория')
ans = []
for pos,val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if val[0] != 'р' and val[0] != 'т' and val[0] != 'я' and val.count('и') >= 2 and pos % 2 != 0:
        ans += [pos]
print(max(ans))