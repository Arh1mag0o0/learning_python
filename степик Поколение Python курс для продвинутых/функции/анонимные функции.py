from functools import reduce

def evaluate(coefficients, x):
    numbers = list(range(len(coefficients)))[::-1]
    out = map(lambda v, a: a * x**v, numbers, coefficients)
    return reduce(lambda a, b: a + b, out, 0)

mas = [int(i) for i in input().split()]
value = int(input())
print(evaluate(mas, value))