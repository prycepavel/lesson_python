motion_data = {
    'distance': 10
}

race_data = {
    'speed': 60,
    'time': 10
}

computer_parts = {
    'processor': 25000,
}


def route_info(significance):
    if 'distance' in significance and isinstance(significance['distance'], int):
        info = f"Distance to your destination is {significance['distance']}"
    elif 'speed' in significance and 'time' in significance:
        if isinstance(significance['speed'], int) and isinstance(significance['time'], int):
            distance = significance['speed'] * significance['time']
            info = f"Distance to your destination is {distance}"
    else:
        info = f"No distance info available"

    return info


print(route_info(motion_data))
print(route_info(race_data))
print(route_info(computer_parts))
