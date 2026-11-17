student = [("Анна", 16),("Бронислав", 15),("Федот", 18)]
# print(max(student),key= lambda x: x[0] for i in range(student): if x[1])
print(max(student, key= lambda x: x[1])[0])

#
# ('anna', 16)  ('bronislav', 15)  ('fedot', 18)