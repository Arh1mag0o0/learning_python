s1 = input().lower()
for i in '.,;:-?!':
	while s1.find(i) != -1:
		s1 = s1[:s1.find(i)] + s1[s1.find(i)+1:]
s1 = s1.split()
myset = set()
for i in s1:
    myset.add(i)
print(len(myset))
