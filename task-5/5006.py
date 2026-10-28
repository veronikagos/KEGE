ans = []
for n in range(0,10000):
    r = f'{n:b}'
    if r.count('1') % 2 == 0:
        r = '10' + r[2:] + '0'
    else:
        r = '11' + r[2:] + '1'
    r = int(r,2)
    if r >= 16:
        ans += [n]
print(min(ans))