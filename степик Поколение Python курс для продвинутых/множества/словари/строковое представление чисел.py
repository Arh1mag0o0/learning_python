number = {1: 'one', 
          2: 'two',
          3: 'three',
          4: 'four',
          5: 'five',
          6: 'six',
          7: 'seven',
          8: 'eight',
          9: 'nine',
          0: 'zero'}
n = int(input())
s = []
while n > 0:
    s.append(number[n % 10])
    n = n // 10
print(*s[-1::-1])