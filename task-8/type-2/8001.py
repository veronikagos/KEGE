from itertools import product

cnt = 0
for val in product('вишня', repeat=6):
    val = ''.join(val)
    if val.count('в') <= 1 and val[0] != 'ш' and val[-1] not in 'яи':
        cnt += 1
print(cnt)