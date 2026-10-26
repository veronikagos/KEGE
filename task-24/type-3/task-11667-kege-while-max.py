with open(r'..\task-files\24_11667.txt') as file:
    data = file.readline()

data = '******INFINITY***INFINITY******INFINITY************************'
l = r = cnt = ans = 0
len_data = len(data)
while r < len_data - 6:
    if cnt <= 1:
        if data[r:r+8] == 'INFINITY':
            cnt += 1
        r += 1
    else:
        if data[l:l+8] == 'INFINITY':
            cnt -= 1
        l += 1
    ans = max(ans, r - l + 6)
print(ans)
