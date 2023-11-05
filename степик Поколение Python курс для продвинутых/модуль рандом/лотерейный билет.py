import random
s_out = []
value = [i for i in range(1, 50)]
for _ in range(7):
    a = value.pop(random.randrange(len(value)))
    s_out.append(a)
s_out.sort()
print(*s_out)