def my_cars(cars):
    if 'bmv' not in cars:
        raise TypeError("Автомобиль не вернулся в гараж")
    elif 'ford' not in cars:
        raise TypeError("Автомобиль не вернулся в гараж")
    elif 'lada' not in cars:
        raise TypeError("Автомобиль не вернулся в гараж")
    else:
        return f"Автомобили '{cars[0]}', '{cars[1]}', '{cars[2]}' вернулись в гараж"


print(my_cars(['bmv', 'ford', 'lada']))

try:
    print(my_cars(['bmv', 'ford']))
except TypeError as e:
    print(e)
