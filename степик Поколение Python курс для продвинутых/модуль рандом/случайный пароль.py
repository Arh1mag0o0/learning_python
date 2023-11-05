import random

length = int(input())    # длина пароля
s = ''
for i in range(length):
    if i % 2 == 0:
        s = s + chr(random.randrange(65, 91))
    else:
        s = s + chr(random.randrange(97, 123))
print(s)