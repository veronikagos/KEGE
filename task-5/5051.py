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
    if n % 3 == 0:
        r = '1' + r + '02'
    else:
        r += convert(n % 3 * 5, 3)
    r = int(r,3)
    if n in (11,12):
        print(n, r)
    if r >= 177:
        ans += [n]
print(min(ans))