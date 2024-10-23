def get_posts_info(name, posts_qty): # Порядок следования аргументов не важен
  info = f"{name} wrote {posts_qty} posts"
  return info

print(get_posts_info(name='Name', posts_qty='25')) # Аргументы с ключевыми словами