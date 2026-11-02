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
    if sum(map(int,r)) % 3 == 0:
        r = r.replace('1','*')
        r = r.replace('0', '1')
        r = r.replace('*', '0')
        r = '10' + r
    else:
        r = '22' + r[2:] + '101'
        r = r[::-1]
    r = int(r,3)
    if r > 314:
        ans.append([r,n])
print(min(ans))