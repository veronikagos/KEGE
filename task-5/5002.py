ans = []
for N in range(1,10000):
    R_1 = bin(N)[2:]
    R = f'{N:b}'
    if N % 2 == 0:
        R = '1' + R + '0'
    else:
        R = '11' + R + '11'
    R = int(R,2) # перевод из 2 системы в 10
    if R > 52:
        ans.append(R)
print(min(ans))
