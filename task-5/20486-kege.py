ans = []
for n in range(1,10000):
    r = f'{n:b}'
    if n % 2 == 0:
        r = r + r[:3]
    else:
        r = '1' + r +'01'
    r = int(r,2)
    if r > 600:
        ans += [r]
print(min(ans))