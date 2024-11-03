# Несколько блоков except с разными ошибками
try:
    print(10 / 0)
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)

print('Continue...')
