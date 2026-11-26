from string import printable

for x in range(0,22):
    num_1 = int(f'12313{printable[x]}57', 22)
    num_2 = int(f'1{printable[x]}34561', 22)
    num = num_1 + num_2
    if num % 21 == 0:
        print(num // 21)