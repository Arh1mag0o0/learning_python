import random

n = int(input())

for _ in range(n):
    if random.random() > 0.5:
        print('Орел')
    else:
        print('Решка')