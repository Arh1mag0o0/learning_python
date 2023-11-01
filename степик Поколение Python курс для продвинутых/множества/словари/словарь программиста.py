n = int(input())
s_dict = {}
for i in range(n):
    s_input = input().split(': ')
    s_dict[s_input[0].lower()] = s_input[1]
m = int(input())
for i in range(m):
    s_search = input().lower()
    if s_search in s_dict:
        print(s_dict[s_search])
    else:
        print('Не найдено')