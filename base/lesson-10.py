# Цикл while

# Нахождение суммы цифр числа любой длинны

num = 123
summ = 0
while num > 0:
    summ += num % 10
    num //= 10
print(summ)

# Цикл for

# range(n, m, k) - создаёт числовой диапозон от n до m с шагом k
print(*range(1,5)) # 1,2,3,4
print(*range(10)) # 0,1,2,3,4,5,6,7,8,9
print(*range(4,10,2)) # 4,6,8

for i in range(5):
    print(i)

data = ['User1','User2','User3']
for i in data:
    print(i)