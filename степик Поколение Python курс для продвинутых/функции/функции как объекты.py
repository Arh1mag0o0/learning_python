def comparator(number):
    out = 0
    for i in number:
        out += int(i)
    return out

numbers = [i for i in input().split()]
numbers.sort(key=comparator)
for i in range(len(numbers-1)):
    if comparator(numbers[i]) == comparator(numbers[i+1]) and int(numbers[i]) > int(numbers[i+1]):
        numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
print(numbers)