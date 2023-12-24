


with open('goats.txt', 'r', encoding='utf-8') as file_input, open('answer.txt', 'w', encoding='utf-8') as file_out:
    colors_goats = {}
    s = file_input.readline()
    check = 0
    while s != 'GOATS':
        s = file_input.readline().rstrip()
        colors_goats[s] = 0
    for i in file_input:
        colors_goats[i.rstrip()] += 1
        check += 1
    for i in colors_goats:
        if int(colors_goats[i] / check * 100) > 7:
            file_out.write(i + '\n')
    
        