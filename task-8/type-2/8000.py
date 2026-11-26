from itertools import product

cnt = 0
for val in product('школа', repeat=3):
    val = ''.join(val)
    if val.count('к') == 1:
        cnt += 1
print(cnt)