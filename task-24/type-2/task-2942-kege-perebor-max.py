with open(r'..\task-files\24_2942.txt') as file:
    data = file.readline()

cnt = ans = i = 0
len_data = len(data) - 1
while i < len_data:
    if data[i:i+2] in 'AB AC':
        cnt += 1
        i += 2
        ans = max(ans, cnt)
    else:
        i += 1
        cnt = 0
print(ans)