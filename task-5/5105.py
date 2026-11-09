ans = []
for k in [1666]:
    s = sum(map(int,str(k)))
    m = max(map(int,str(k)))
    n = min(map(int,str(k)))
    p1 = s - m
    p2 = s - n
    if p1 <= p2:
        l = str(p1) + str(p2)
    else:
        l = str(p2) + str(p1)
    if int(l) == 1318:
        ans += [k]
print(min(ans))