ans = []
for n in range(1,10000):
    r = f'{n:b}'
    if n % 8 == 0:
        r += r[-2:]
    else:
        r = r + f'{(n % 8) * 2:b}'
    r = int(r,2)
    if r > 3000:
        ans += [n]

print(min(ans))