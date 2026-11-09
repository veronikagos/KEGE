res = []
num = 11*15**65 + 18*15**38 - 14*15**17 + 19*15**11 + 18338
while num:
    res = [num % 15] + res
    num //= 15
print(len(set(res)))