ans = []
for x in range(0,100):
    res = ''
    num = 3*7**(x + 1) + 13*7**(x + 2) + 31*7**(3*x) + 7**(2*x)
    while num:
       res = str(num % 7) + res
       num //= 7
    if sum(map(int,res)) == 18:
        ans += [x]
print(min(ans))