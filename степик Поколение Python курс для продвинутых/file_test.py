import random

with open('file.txt', 'r', encoding='utf-8') as file:
    buf_first_name = file.readlines()

with open('file.txt', 'r', encoding='utf-8') as file:
    buf_last_name = file.readlines()
    
list_first_names = [i.rstrip() for i in buf_first_name]
list_last_names = [i.rstrip() for i in buf_last_name]

out_first_names = random.choices(list_first_names, 3)
out_last_names = random.choices(list_last_names, 3)
for a, b in out_first_names, out_last_names:
    print(a, b)