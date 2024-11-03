# 1. Создайте функцию image_info с одним параметром типа dict
# 2. Функция ожидает словарь, в котором должно быть как минимум два ключа:
#     image_id,
#     image_title
# 3. Функция должна возвращать строку такого вида "Image 'my cat' has id 5136"
# 4. Если хотя бы одного из этих ключей в словаре нет, функция должна генерировать ошибку TypeError
# 5. Вызовите функцию и корректно обработайте ошибку в случае возникновения

def image_info(img):
    # Проверяет есть ли нужные ключи в словаре
    if ('image_id' not in img) or ('image_title' not in img):
        # формирует нужную ошибку
        raise TypeError("Keys image_id and image_title my be present")

    return f"Image {img['image_title']} has id {img['image_id']}"


print(image_info({'image_title': 'My cat', 'image_id': 123}))

try:
    print(image_info({'image_title': 'My cat'}))
except TypeError as e:
    print(e)
