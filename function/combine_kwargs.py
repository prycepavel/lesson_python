def get_posts_info(**person): # Объединяет множество аргументов в один словарь
  print(person)
  print(type(person))
  info = (
    f"{person['name']} wrote " # Если не ставить запятую Python объеденит две строки в одну
    f"{person['posts_qty']} posts"
  )
  return info

print(get_posts_info(name='Name', posts_qty='25'))