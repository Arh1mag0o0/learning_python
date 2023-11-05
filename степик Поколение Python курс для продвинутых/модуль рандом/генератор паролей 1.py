import random
import string

def generate_password(length):
    s_out = []
    s_E = ''.join(set(string.ascii_lowercase) - set('ol'))
    s_e = ''.join(set(string.ascii_uppercase) - set('OI'))
    s_1 = ''.join(set(string.digits) - set('10'))
    s_out.append(random.choice(s_E))
    s_out.append(random.choice(s_e))
    s_out.append(random.choice(s_1))
    slovar = ''.join((set(string.ascii_letters) | set(string.digits)) - set('lI1oO0'))
    for _ in range(length-3):
        s_out.append(random.choice(slovar))
    random.shuffle(s_out)
    return ''.join(s_out)

def generate_passwords(count, length):
    for _ in range(count):
        print(generate_password(length))

n, m = int(input()), int(input())

generate_passwords(n, m)