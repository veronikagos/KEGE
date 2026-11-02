ans = []
for n in range(1,10000):
    r = f'{n:b}'
    if n % 2 == 0:
        r = '11' + r + '11'
    else:
        r = '1' + r + '00'
    r = int(r,2)
    if r <= 113:
        ans += [r]
print(max(ans))