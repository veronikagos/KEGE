from itertools import *

# Формирует все возможные комтбинации с повторением
for val in product('123',repeat=2):
    val = ''.join(val) # Обьединяет все символы кортежа в строку

for pos, val in enumerate(product('123', repeat=3), start=1):
    val = ''.join(val)
    print(pos,val)