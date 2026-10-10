# Task of conditional expressions

from random import *

num = randint(100,999)
if num % 10 == 1 or num % 10 == 3 or num % 10 == 5 or num % 10 == 7 or num // 100 == 1 or num // 100 == 3 or num // 100 == 5 or num // 100 == 7 or num % 100 //10 == 7 or num % 100 //10 == 5 or num % 100 //10 == 3 or num % 100 //10 == 1:
    print(num)
else:
    print('Число не содержит ни одну из цифр 1,3,5 или 7')

# Задача на тернарного оператора
num_1 = int(input())
print(num_1 + 1 if num_1 % 2 == 0 else num_1)
