with open('class_scores.txt') as inp_file, open('new_scores.txt', 'w') as out_file:
    for s in inp_file:
        s, i = s.rstrip().split()
        if int(i) > 95:
            i = 95
        out_file.write(s + ' ' + str(int(i)+5)+'\n')