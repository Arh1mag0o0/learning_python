with open('population.txt', 'r', encoding='utf-8') as file:
    file_text = file.readlines().rstrip()
    
s = filter(lambda x: x[0][0] == 'G' and int(x[1]) > 500000, ([i.split('\t') for i in file_text]))
for i in s:
    print(i[0])