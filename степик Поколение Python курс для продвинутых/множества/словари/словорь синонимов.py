n = int(input())
my_sloar = {}
for i in range(n):
    s_in = input().split()
    my_sloar[s_in[0]] = s_in[1]
    my_sloar[s_in[1]] = s_in[0]
print(my_sloar[input()])