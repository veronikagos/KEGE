from re import *

with open(r'../task-files/24_19967.txt') as file:
    data = file.readline()

num = r'([1-9][0-9]*|0)'
pattern = rf'AFD({num}[+*])+{num}'

matches = [math.group() for math in finditer(pattern, data)]
print(len(max(matches, key=len)))