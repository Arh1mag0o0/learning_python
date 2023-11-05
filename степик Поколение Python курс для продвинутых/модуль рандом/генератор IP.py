import random

def generate_ip():
    s_list = []
    for _ in range(4):
        s_list.append(str(random.randrange(256)))
    return '.'.join(s_list)

print(generate_ip())

