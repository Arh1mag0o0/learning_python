import random

word = input()
s = list(word)
random.shuffle(s)
print(*s, sep='')
    