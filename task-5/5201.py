from string import printable

def convert(num,sys):
    res = ''
    while num:
        res = printable[num % sys] + res
        num //= sys
    return res if res else '0'

ans = []
for n in range(1,10000):
    r = convert(n,4)
    if sum(map(int,r)) % 2 == 0:
        r += r[-2:]
    else:
        r = '2' + r + '0'
    r = int(r,4)
    if r % 2 == 0 and r > 120:
        ans += [r]
print(min(ans))