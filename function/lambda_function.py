def greeting(greet):
    return lambda name: f"{greet}, {name}"


morning_greeting = greeting('Good morning')
print(morning_greeting('Batman'))

evening_greeting = greeting('Good evening')
print(evening_greeting('Batman'))

air = greeting('Air')
print(air('Batman'))
