ans = []
for x in range(1,2031):
    cnt = 0
    num = 7**170 + 7**100 - x
    while num:
        if num % 7 == 0:
            cnt += 1
        num //= 7
    if cnt == 71:
        ans += [x]
print(max(ans))