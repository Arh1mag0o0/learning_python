abscissas = [float(i) for i in input().split()]
ordinates = [float(i) for i in input().split()]
applicates = [float(i) for i in input().split()]
print(all(map(lambda x: x[0]**2 + x[1]**2 + x[2]**2 <= 2**2, zip(abscissas, ordinates, applicates))))


ip = [i.lstrip('0') for i in input().split('.')]
print(all(map(lambda x: x == '' or  (x.isdigit() and int(x) <= 255), ip)))

def prth(x):
    if '0' in str(x):
        return False
    for i in str(x):
        if x % int(i) != 0:
            return False
    return True


a, b = int(input()), int(input())
print(*(filter(lambda i: all([i % int(x) == 0 for x in str(i)]), list(range(a, b)))))
