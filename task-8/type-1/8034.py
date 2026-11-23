from itertools import *
alph = sorted('фокус')
ans = []
for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if val.count('ф') == 0 and 'ф' not in val and val.count('у') == 2:
       ans += [pos]
print(max(ans))