import random

s_out = set()

while len(s_out) != 100:
    s_out.add(random.randint(1000000, 9999999))
    
print(*s_out, sep='\n')