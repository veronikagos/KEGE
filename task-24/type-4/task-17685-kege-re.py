# from re import *
#
# with open(r'../task-files/24_17685.txt') as file:
#     data = file.readline()
#
# # data = '05486++10398*945206*+94859***0087+138*0'
# num = r'([1-9][0-9]*|0)'
# pattern = rf'({num}(\+|\*))+{num}'
#
# matches = [math.group() for math in finditer(pattern, data)]
# ans = 0
# for i in matches:
#     len_i = len(i)
#     if eval(i) == 0:
#         ans = max(ans,len_i)
#     elif len_i > ans:
#         for l in range(len_i - 1):
#             if i[l] in '+*' or i[l] == '0' and i[l + 1] in '0123456789':
#                 continue
#             for r in range(len_i - 1, l, -1):
#                 if i[r] in '+*':
#                     continue
#                 if eval(i[l:r + 1]) == 0:
#                     ans = max(ans, r - l + 1)
#                     break
#             if len_i - l < ans: # необезательно, просто ускоряет работу
#                 break
# print(ans)


#############################################3

from re import *

with open(r'../task-files/24_17685.txt') as file:
    data = file.readline()

# data = '05486++10398*945206*+94859***0087+138*0'
num = r'([1-9][0-9]*|0)'
null = rf'({num}\*)*0(\*{num})*'
pattern = rf'({null}\+)+{null}'

matches = [math.group() for math in finditer(pattern, data)]

print(len(max(matches, key=len)))