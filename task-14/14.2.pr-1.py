from string import printable

for x in printable[:20]:
    num_1 = int(f'627{x}j8', 20)
    num_2 = int(f'h45i{x}5hij', 20)
    num_3 = int(f'4idb49j{x}7', 20)
    num = num_1 + num_2 + num_3
    if num % 19 == 0:
        print(num // 19)