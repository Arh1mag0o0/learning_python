n = int(input())
my_dict = dict()
WRE = {'write': 'W', 'read': 'R', 'execute': 'X'}
for _ in range(n):
    s = input().split()
    my_dict[s[0]] = s[1:]
for _ in range(int(input())):
    a, b = input().split()
    if WRE[a] in my_dict[b]:
        print('OK')
    else:
        print('Access denied')