# put your python code here
n, m, k, x, y, z, t, a = int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input())
two_b = n + k - z + n + m - x + m + k - y - 3 * t
one_b = n + m + k - two_b * 2 - 3 * t
null_b = a - one_b - two_b - t
print(one_b, two_b, null_b, sep='\n')