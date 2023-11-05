import random
import string

def generate_index():
    s = string.ascii_uppercase
    s_out = []
    s_out.append(s[random.randrange(len(s))] + s[random.randrange(len(s))] + str(random.randrange(100)))
    s_out.append(str(random.randrange(100)) + s[random.randrange(len(s))] + s[random.randrange(len(s))])
    return '_'.join(s_out)

print(generate_index())

