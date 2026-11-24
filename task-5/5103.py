ans = []
for n in range(1,10000):
    r = f'{n:b}'
    if n % 2 == 0:
        r += '0'
    else:
        r += '1'
    if r.count('1') % 3 == 0:
        r = '11' + r[2:]
    else:
        r = '10' + r[2:]
    r = int(r,2)
    if n in (6,3):
        print(n,r)
    if r >= 26:
        ans += [n]
print(min(ans))