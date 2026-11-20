cnt = 0
for n in range(300,401):
    n = str(n)
    r = sorted(list(n))
    r_max = int(r[2] + r[1])
    if r[0] == '0':
        r_min = None
    else:
        r_min = int(r[0] + r[1])
        if r_max - r_min == 20:
            cnt += 1
print(cnt)