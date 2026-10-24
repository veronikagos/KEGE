with open(r'..\task-files\24_19254.txt') as file:
    data = file.readline()

l = r = cnt = ans = 0
len_data = len(data)
while r < len_data:
    if cnt <= 80:
        if data[r:r+4] == 'FSRQ':
            cnt += 1
        r += 1
    else:
        if data[l:l+4] == 'FSRQ':
                cnt -=1
        l += 1
    ans = max(ans, r - l + (2 if r not in range(len_data - 4, len_data + 1) else 0))
print(ans)