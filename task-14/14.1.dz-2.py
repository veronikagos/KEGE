res = ''
num = 51*7**12 - 7**3 - 22
while num:
    res = str(num % 7) + res
    num //= 7
print(sum(map(int,res)))