import random

names_1 = [input() for _ in range(int(input()))]
names_2 = [i for i in names_1]
random.shuffle(names_2)
flag = True
t = 0
while flag:
    for i in range(len(names_1)):
        if names_1[i] == names_2[i]:
            random.shuffle(names_2)
            t = 0
            break
        else:
            t += 1
        if t == len(names_1):
            flag = False
for i in range(len(names_1)):
    print(names_1[i], '-', names_2[i])