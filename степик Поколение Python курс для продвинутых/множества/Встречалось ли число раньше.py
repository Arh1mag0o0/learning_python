s = [int(i) for i in input().split()]
mySet = set()
for i in s:
    if i in mySet:
        print('YES')
    else:
        mySet.add(i)
        print('NO')