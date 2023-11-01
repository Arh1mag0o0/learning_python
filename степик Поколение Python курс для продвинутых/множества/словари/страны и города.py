city = {}
for i in range(int(input())):
    s_in = input().split()
    for j in s_in:
        city[j] = s_in[0]
for i in range(int(input())):
    print(city[input()])