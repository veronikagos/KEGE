from itertools import *
alph = sorted('алгоритм')
ans = []
for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if val[0] not in ('аг') and val.count('р') >= 2 and pos % 2 == 0:
        ans.append([pos, val])
print(min(ans))