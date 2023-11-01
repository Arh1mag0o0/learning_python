s = input().split()
out = []
buf = {}
for i in s:
    if i not in buf:
        buf[i] = 0
        out.append(i)
    else:
        buf[i] += 1
        out.append(i + '_' + str(buf[i]))
print(*out)