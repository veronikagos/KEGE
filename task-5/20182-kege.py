from string import printable
def convert(num,sys):
    res = ''
    while num:
        res = printable[num % sys] + res
        num //= sys
    return res if res else '0'

ans = []
for n in range(1,10000):
    r = convert(n,3)
    if sum(map(int,r)) % 2 == 0:
        r = '12' + r[2:] + '0'
    else:
        r = '10' + r[2:] + '2'
    r = int(r,3)
    if r > 105:
        ans += [n]
print(min(ans))