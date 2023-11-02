s_in = input()
s_set = set(s_in)
word_dict = dict()
for _ in range(int(input())):
    a, number = input().split(': ')
    word_dict[int(number)] = a
for i in s_set:
    s_in = s_in.replace(i, word_dict[s_in.count(i)])
print(s_in)