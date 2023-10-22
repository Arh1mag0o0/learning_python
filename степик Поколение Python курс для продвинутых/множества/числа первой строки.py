s1 = set([int(i) for i in input().split()])
s2 = set([int(i) for i in input().split()])
s1 -= s2
s1 = sorted(s1)
print(*s1)