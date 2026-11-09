with open(r'..\task-files\24_865.txt') as file:
    data = file.readline()

ans = cnt = 0
for i in range(len(data)):
    if data[i] == 'C' or data[i] == 'F': # if data[i] in 'CF':
        cnt = 0
    else:
        cnt += 1
    ans = max(ans, cnt)
print(ans)