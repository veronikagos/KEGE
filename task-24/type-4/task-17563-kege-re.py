from re import *
with open(r'..\task-files\24_17563.txt') as file:
    data = file.readline()

pattern = r'([7-9][07-9]*[\*-])+[7-9][07-9]*'
matches = [match.group() for match in finditer(pattern, data)]

print(len(max(matches,key=len)))
