with open(r'..\task-files\24_4627.txt') as file:
    data = file.readline()

ans = cnt = i = 0
len_data = len(data) - 2
while i < len_data:
    if data[i:i+3] in 'NPO PNO':
        cnt += 1
        i += 3
        ans = max(ans,cnt)
    else:
        cnt = 0
        i += 1
print(ans)