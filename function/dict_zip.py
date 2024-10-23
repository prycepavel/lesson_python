def merge_list_to_dict(list_one, list_two):
  zipped_seq = zip(list_one, list_two)
  return dict(zipped_seq)

print(merge_list_to_dict(list_one=[1, 2, 3], list_two=[10, True, 'int']))
print(merge_list_to_dict([10, True, 'int'], list_two=[1, 2, 3]))