with open(r'..\task-files\24_9753.txt') as file:
    data = file.readline()

l = cnt = ans = 0
for r in range(len(data)):
    if data[r] == 'Y': cnt += 1
    while cnt > 150:
        if data[l] == 'Y': cnt -= 1
        l += 1
    if cnt == 150:
        ans = max(ans, r - l + 1)
print(ans)

