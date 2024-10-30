button_default = {
    'text': 'Ok',
    'color': 'black',
    'width': 0,
    'height': 0,

}
button_style = {
    'width': 200,
    'height': 300,
    'color': 'grey'
}

# Один из вариантов объединения словарей
# button = {
#     **button_info,
#     **button_style
# }

# Приоритет по значениям при создании нового словаря,
# получит тот словарь который стоит первый при объединении,
# порядок следования операндов играет роль
button_one = button_default | button_style
button_two = button_style | button_default

print(button_one)
print(button_two)
