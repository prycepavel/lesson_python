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
        return f"Distance to your destination is {significance['distance']}"

    if 'speed' in significance and 'time' in significance:
        if isinstance(significance['speed'], int) and isinstance(significance['time'], int):
            distance = significance['speed'] * significance['time']
            return f"Distance to your destination is {distance}"

    return f"No distance info available"


print(route_info(motion_data))
print(route_info(race_data))
print(route_info(computer_parts))
