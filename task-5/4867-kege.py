ans = []
for n in range(2,10000):
    sum_1 = sum(map(lambda x: int(x) if int(x) % 2 == 0 else "0",str(n))) # ошибка
    sum_2 = sum(map(int, str(n)[1::2]))
    r = abs(sum_1-sum_2)
    if r == 9:
        print(n)
        break