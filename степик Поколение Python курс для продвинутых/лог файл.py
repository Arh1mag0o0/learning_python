def time(in_time):
    hour, minets = in_time.split(':')
    return int(hour) * 60 + int(minets)

def read_name_time(s):
    name, time1, time2 = s.rstrip().split(', ')
    return name, abs(time(time2)-time(time1))

with open('logfile.txt', 'r', encoding='utf-8') as file_input, open('output.txt', 'w', encoding='utf-8') as file_out:
    for i in file_input:
        value, key = read_name_time(i)
        if key >= 60:
            file_out.write(value + '\n')
            