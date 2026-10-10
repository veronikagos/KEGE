with open(r'..\task files\24_21717.txt') as file:
    data = file.readline()

data = data.split('RSQ')
ans = 10**10
for i in range(1, len(data)-128-1):
    line = 'RSQ' + 'RSQ'.join(data[i:i + 129]) + 'RSQ'
    for j in range(len(data[i+129])):
       if data[i+129][j] != 'Q':
           ans = min(ans, len(line) + j + 1)
           break
    else:
        ans = min(ans, len(line) + len(data[i+129]) + 1)
print(ans)