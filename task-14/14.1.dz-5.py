for i in range(0,41):
    n = i
    res = ''
    while n:
        res = str(n % 2) + res
        n //= 2
    if res[-4:] == '1011':
        print(i)