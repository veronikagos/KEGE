ans = []
for n in range(1,10000):
    r = f'{n:b}'
    if n % 2 == 0:
        r = '10' + r
    else:
        r = '1' + r + '01'
    r = int(r,2)
    if n in (4,5):
        print(n,r)
    if n >= 17:
        ans += [r]
print(min(ans))