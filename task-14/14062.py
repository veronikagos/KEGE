from string import printable
for x in range(1,22):
    num_1 = int(f'27{printable[x]}98876',22)
    num_2 = int(f'26{printable[x]}51', 22)
    num_3 = int(f'711{printable[x]}5', 22)
    num = num_1 + num_2 + num_3
    if num % 21 == 0:
        print(num // 21)