s = input()
s_dict = {}
for i in s.split():
    if i not in s_dict:
        s_dict[i] = 1
        print(1, end=' ')
    else:
        s_dict[i] += 1
        print(s_dict[i], end=' ')