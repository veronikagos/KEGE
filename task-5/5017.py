ans = []
for n in range(0,10000):
    r = f'{n:b}'
    if n % 3 == 0:
        r = r + r[-3:]
    else:
       r = r + f'{n % 3 * 3:b}'
    r = int(r,2)
    if r > 76:
        ans += [n]

print(min(ans))