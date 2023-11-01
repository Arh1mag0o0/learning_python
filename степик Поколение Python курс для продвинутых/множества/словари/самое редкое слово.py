s_p = '.,!?:;-'
s = input().lower()
for i in s_p:
    if i in s:
        s = s.replace(i, '')
s_tuple = set(s.split())
minimum = 100
s = s.split()
buf = 'a'
for i in s_tuple:
    if s.count(i) <= minimum:
        if  i > buf and s.count(i) == minimum:
            buf = buf
        else:
            buf = i
        minimum = s.count(i)
print(buf)
    