res = ''
num = 5*216**3031 + 4*36**3042 - 3*6**3053 - 3064
while num:
    res = str(num % 6) + res
    num //= 6
summ = sum(map(int,res))
print(summ)