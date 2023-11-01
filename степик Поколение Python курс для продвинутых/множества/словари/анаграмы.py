s_1 = input()
s_2 = input()
Flag = True
for i in s_1:
    if i not in s_2 or s_1.count(i) != s_2.count(i) or len(s_1) != len(s_2):
        Flag = False
        break
if Flag:
    print('YES')
else:
    print('NO')
           
