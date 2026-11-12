from string import printable
num = 282**382 + 9**15 + 2**3
res = ''
cnt_b = 0
cnt_c = 0
while num:
    res = printable[num % 14] + res
    num //= 14
for i in range(len(res)):
    if res[i] == 'b':
        cnt_b += 1
    elif res[i] == 'c':
        cnt_c += 1
print(cnt_b,cnt_c,res)
print(abs(cnt_b - cnt_c))
# 