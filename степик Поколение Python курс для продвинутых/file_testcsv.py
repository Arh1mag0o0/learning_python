import random

def read_csv():
    with open('C:/profil/ /data.csv', 'r') as file:
        text = file.readlines()
    out = list()
    f = list(map(lambda x: x.rstrip(), text))
    key = f[0].split(',')
    for i in f[1:]:
        value = i.split(',')
        out.append(dict(zip(key, value)))
    return out

mass = [random.randint(111, 777) for _ in range(25)]
with open('random.txt', 'w', encoding='utf-8') as file:
    for i in mass:
        file.writelines(str(i) + '\n')





