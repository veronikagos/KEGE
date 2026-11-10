from string import printable
num = 4**36 + 3*4**20 + 4**15 + 2*4**7 + 49
res = ''
while num:
    res = printable[num % 16] + res
    num //= 16
print(res)
print(len(set(res)))