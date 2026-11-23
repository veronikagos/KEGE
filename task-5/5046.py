ans = []
for n in range(1,10000):
    r = f'{n:b}'
    if n % 3 == 0:
        r = r + r[-3:]
    else:
        r += f'{n % 3 * 3:b}'
    r = int(r,2)
    # if n in (6,4):
    #    print(n,r)
    ans.append([abs(130 - r),n])
#     if r <= 130:
#         ans.append([r,n])
# print(max(ans))

print(max(ans, key= lambda x:(-x[0],x[1])))