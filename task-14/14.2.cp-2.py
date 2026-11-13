num = 729**8 - 3**18 + 85
res = ''
cnt = 0
while num:
    res = str(num % 9) + res
    num //= 9
for i in range(len(res)):
    if res[i] == '0':
        cnt += 1
print(cnt)