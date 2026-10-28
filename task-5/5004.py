ans = []
for n in range(0,10000):
    r = f'{n:b}'
    if n % 2 == 0:
        r = r + '10'
    else:
        r = '1' + r + '01'
    r = int(r,2)
    if r > 516:
        ans.append(n) # ans += [r]
print(min(ans))