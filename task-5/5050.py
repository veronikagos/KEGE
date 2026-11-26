ans = []
for n in range(1,10000):
    r = f'{n:b}'
    if sum(map(int,r)) % 2 == 0:
        r = '10' + r[2:] + '0'
    else:
        r = '11' + r[2:] + '1'
    r = int(r,2)
    if n in (6,4):
        print(n,r)
    if r <= 19:
        ans += [n]
print(max(ans))