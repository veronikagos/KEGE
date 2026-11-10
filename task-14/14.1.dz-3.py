num_1 = 41
num_2 = 131
for n in range(3,36):
    res_1 = num_1 % n
    res_2 = num_2 % n
    if res_1 == 2 and res_2 == 1:
        print(n)