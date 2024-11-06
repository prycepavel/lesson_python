my_fruits = ['apple', 'banana', 'lime']
# В список можно добавлять новые элементы
apple, banana, lime = my_fruits
print(apple)
print(banana)
print(lime)

my_list = [1, 2, 3]
first, second, third = my_list
# Если поменять переменные местами,
# выводимые значения изменятся.
second, first, third = my_list
print(first)
print(second)
print(third)


my_gadget = ('telephone', 'tablet', 'laptop')
# В кортеж добавлять новые элементы нельзя
telephone, tablet, laptop = my_gadget
print(telephone)
print(tablet)
print(laptop)

my_cars = ['bmw', 'ford', 'lada']
*remaining_cars, lada = my_cars
print(lada)
print(remaining_cars)

# Распаковка словаря
user_profile = {
    'name': 'Tom',
    'comments_qty': 23,
}


def user_info(name, comments_qty=0):
    if not comments_qty:
        return f"{name} has no comments"
    return f"{name} has {comments_qty} comments"


# Варианты запуска функции
print(user_info(**user_profile))
print(user_info(user_profile['name'], user_profile['comments_qty']))
print(user_info(name=user_profile['name'],
                comments_qty=user_profile['comments_qty']))

# Распаковка списка
user_data = ['Jim', 23]


def user_parameters(name, comments_qty=0):
    if not comments_qty:
        return f"{name} has no comments"
    return f"{name} has {comments_qty} comments"


print(user_parameters(*user_data))
print(user_parameters(user_data[0], user_data[1]))
print(user_parameters(name=user_data[0], comments_qty=user_data[1]))

my_name, my_comments_qty = user_data
print(user_parameters(my_name, my_comments_qty))
