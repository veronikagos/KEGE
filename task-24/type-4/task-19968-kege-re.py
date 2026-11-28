from re import *

with open(r'../task-files/24_19968.txt') as file:
    data = file.readline()

num = r'([1-5][0-5]*|0)'
pattern = rf'({num}[+*])+{num}'

matches = [math.group() for math in finditer(pattern, data)]

print(len(max(matches, key=len)))