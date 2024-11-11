my_img = ('1920', '1080')

info = f"{my_img[0]}x{my_img[1]}" if len(
    my_img) == 2 else 'Incorrect image formatting'
print(info)

if len(my_img) == 3:
    new_info = f"{my_img[0]}x{my_img[1]}"
else:
    new_info = 'Incorrect image formatting'
print(new_info)

my_string = 'Чем более послушен человек, тем менее ценна его личность.'
new_string = 'Непостижимый, странный закон: к чувству собственной вины склонны всегда самые невинные.'
print('Строка длинная' if len(new_string) > 79 else 'Строка короткая')
