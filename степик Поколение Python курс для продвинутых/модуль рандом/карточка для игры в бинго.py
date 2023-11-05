import random
value = [i for i in range(1, 76)]
s_out = random.sample(value, 25)
s_out[12] = 0
t = 0
for i in s_out:
    print(str(i).ljust(3), end='')
    t += 1
    if t == 5:
        print()
        t = 0
    

    
    