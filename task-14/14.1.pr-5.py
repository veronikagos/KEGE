from string import printable
n_5 = ''
n_3 = ''
n_16 = ''
for i in range(10000):
    c = a = b = i
    while a:
        n_5 = str(a % 5) + n_5
        a //= 5
    while b:
        n_3 = str(b % 3) + n_3
        b //= 5
    while c:
        n_16 = printable[(c % 16)] + n_16
        c //= 16
    if len(n_5) == 4 and len(n_3) == 5 and n_16[-1] == 'd':
        print(i)