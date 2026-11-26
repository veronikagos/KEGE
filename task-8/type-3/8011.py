from string import printable
from itertools import product

cnt = 0
for val in product(printable[:7], repeat=6):
    val = ''.join(val)
    if val[0] != '0' and val.count('6') == 1:
        for i in printable[:7:2]:
            val = val.replace(i,'*')
        for i in printable[1:7:2]:
            val = val.replace(i, '!')
        if '**' not in val and '!!' not in val:
            cnt += 1
print(cnt)