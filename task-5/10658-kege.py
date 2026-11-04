from string import printable
def convert(num,sys):
    res = ''
    while num:
        res = printable[num % sys] + res
        num //= sys
    return res if res else '0'


ans = []
cnt_1 = 0
cnt_2 = 0
for n in range(11,10000):
    r = convert(n,3)
    for i in range(len(r)):
        if int(r[i]) % 2 == 0:
            cnt_2 += 1
        else:
            cnt_1 += 1
    if cnt_2 > cnt_1:
        r = '22' + r
    else:
        r = '11' + r
    r = int(r,3)
    if r > 100:
        ans += [r]
print(min(ans))