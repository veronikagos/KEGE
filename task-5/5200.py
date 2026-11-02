ans = []
for n in range(1,10000):
    r = f'{n:o}'
    cnt = sum(r.count(i) for i in '0246')
    if cnt % 2 != 0:
        r = r[-3:] + '46'
    else:
        r = f'{n % 8 * 5:o}' + r
    r = int(r,8)
    if r == n:
        ans += [n]
print(min(ans))