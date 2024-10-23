def update_car_info(**car):
  car['is_available'] = True
  return car


car = update_car_info(brand='BMW', price='1500')
print(car)