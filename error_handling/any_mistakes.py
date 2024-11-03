try:
    print(10 / 0)
except Exception as e:
    # Родительский класс для всех ошибок Exception после except,
    # можно использовать когда не знаешь какую ошибку ожидать.
    print(e)
