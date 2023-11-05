import random

n = 10**6
k = 0
s0 = 2*2
for _ in range(n):
    x = random.uniform(0, 1)     # случайное число с плавающей точкой от 0 до 1
    y = random.uniform(0, 1)     # случайное число с плавающей точкой от 0 до 1

    if x**2 + y**2 <= 1:                # если попадает в нужную область
        k += 1

print((k/n)*s0)