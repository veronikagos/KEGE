ans = []
for n in range(1,10000):
    r = f'{n:b}'
    if sum(map(int,r)) % 2 == 0:
        r = '11' + r[2:] + '1'
    elif r.count('0') < r.count('1'):
        r += '0'
    else:
        r += '1'
    r = int(r,2)
    if r > 271:
        ans += [n]
print(min(ans))