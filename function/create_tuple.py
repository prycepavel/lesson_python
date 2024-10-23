def sum_nams(*args): # Собирает множество аргументов в один кортеж
  print(args)
  print(type(args))
  print(args[0])
  return sum(args)

print(sum_nams(2, 3, 7))
