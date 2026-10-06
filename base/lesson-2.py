# Типы данных

# Целое число / Interger / int
my_int = 67
print(type(my_int))

# Дробное, вещественное, с плавающей точкой число / Float / float
my_float = 15.05
print(type(my_float))

# Строка / String / str
my_str_1 = "Hello"
my_str_2 = 'World'
print(type(my_str_1))


# Примеры сложения переменных
# print(my_str_1 + my_str_2) - две строки ОК
# print(my_int + my_float) - два числа ОК
# print(my_str_1 + my_int) - строка и число, ошибка конкатенации (объединение строк)
# print(my_int + my_str_1) - число и строка, ошибка сложения


# Список / list / list
my_list = ['Nika', 17, 200.5]
print(type(my_list))
# Обращение к содержимому
print(my_list[0])
print(type(my_list[0]))


# Кортеж / Tuple / tuple
my_typle = ('Nika', 17, 200.5)
print(type(my_typle))