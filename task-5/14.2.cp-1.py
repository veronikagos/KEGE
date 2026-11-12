from string import printable
def convert(num,sys):
    res = ''
    while num:
        res = printable[num % sys] + res
        num //= sys
    return res if res else ''
ans = []
for n in range(0,10000):
    r = convert(n,3)
    if sum(map(int,r)) % 3 == 0:
        r += '212'
    else:
        r += convert((sum(map(int,r))) * 2,3)
    r = int(r, 3)
    if r > 490:
        ans += [r]
print(min(ans))