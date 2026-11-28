from itertools import product

ans = []
alph = sorted('солнце')
for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if pos % 2 != 0 and val[0] not in 'цн' and val.count('ц') == 1 and val.count('н') == 1:
        ans.append([pos,val])
print(max(ans))