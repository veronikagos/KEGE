with open(r'..\task-files\24_4602.txt') as file:
    data = file.readline()

for i in 'BCD':
    data = data.replace(i, '*')
for i in 'AO':
    data = data.replace(i, '!')
data = data.replace('*!', '+')
data = data.replace('*',' ').replace('!', ' ')
data = data.split()
print(len(max(data, key=len)))