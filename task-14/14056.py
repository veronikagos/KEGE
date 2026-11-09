cnt = 0
res = []
num = 5*1296**2021 - 4*216**2022 + 3*36**2023 - 2*6**2024 - 2025
while num:
    res = [num % 36] + res
    num //= 36
print(res)
for i in range(len(res)):
    if res[i] % 2 == 0:
        cnt += 1
        print(res[i])
print(cnt)