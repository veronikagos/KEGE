from string import printable
def convert(num,sys):
    res = 0
    for i in range(len(num)):
        res += int(printable.index(num[i]))*sys**(len(num)-1-i)
    return res
cnt = 0
for x in range(10,67):
    for y in range(0, x):
        num_1 = convert(f'73{printable[x]}1{printable[y]}', 67)
        num_2 = convert(f'49{y}6', x)
        num = num_1 + num_2
        if num:
            cnt += 1
print(cnt)