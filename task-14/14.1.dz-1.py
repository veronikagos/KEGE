res = ''
num = 16**820 - 2**761 + 14
while num:
    res = str(num % 4) + res
    num //= 4
print(res.count('0'))