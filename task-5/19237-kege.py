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
        r += r[-2:]
    else:
        r += convert(sum(map(int,r)),3)
    r = int(r,3)
    if r % 2 == 0 and r > 220:
        ans += [r]
print(min(ans))