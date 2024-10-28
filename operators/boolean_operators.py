my_list_one = ['a', 'b']
my_list_two = [1, 2]
my_dict = {}

# Оператор and (и)
# Если первое значение ложное, возвращает второе
print(my_dict and my_list_one)
# Если первое значение истинное, возвращает второе
print(my_list_one and my_list_two)
# Если одно из значений ложное, всё выражение будет ложным
print(bool(my_list_one and my_dict))
# Если оба значения истинные, всё выражение будет истинным
print(bool(my_list_one and my_list_two))


# Выражение с оператором or (или) возвращает первое правдивое значение
# print(my_list_one or my_list_two)

# not Оператор отрицания
# print(not my_list_one)
# print(not my_list_two)
# print(not not my_list_two)
