from string import printable

def convert(num,sys):
    res = ''
    while num:
        res = printable[num % sys] + res
        num //= sys
    return res if res else '0'

ans = []
for n in range(1,10000):
    r = convert(n,5)
    if sum(map(int,r)) % 5 == 0:
        r = r.replace('0','*')
        r = r.replace('1', '0')
        r = r.replace('*', '1')
        r += '14'
    else:
        r = '44' + r[2:] + '33'
        r = r[::-1]
    r = int(r,5)
    if r > 370:
        ans.append([r,n])
print(min(ans))