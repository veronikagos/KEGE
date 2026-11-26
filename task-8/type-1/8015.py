from itertools import product

ans = []
alph = sorted('цапля')
for pos,val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if val.count('а') <= 1 and val.count('ц') == 2 and 'л' not in val:
       ans.append(pos)
print(min(ans))