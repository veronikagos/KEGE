ans = []
for n in range(0,10000):
    r = f'{n:b}'
    r = r + str(r.count('1') % 2)
    r = r + str(r.count('1') % 2)
    r = int(r,2)
    if r > 77:
        ans += [n]
print(min(ans))