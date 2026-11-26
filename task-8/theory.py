from itertools import *

# Буквы в алфавитном порядке
alph = sorted('фокус')

# Буквы в обратном алфавитном порядке
alph = sorted('фокус', revers=True)

# Формирует все возможные комтбинации с повторением
for val in product('123',repeat=2):
    val = ''.join(val) # Обьединяет все символы кортежа в строку

for pos, val in enumerate(product('123', repeat=3), start=1):
    val = ''.join(val)
    print(pos,val)
