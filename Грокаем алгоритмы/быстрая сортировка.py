# Упражения на рекурсию 4.1-4.3

def sum_elem(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + sum_elem(arr[1:])

def kolvo_elem(arr):
    if arr == []:
        return 0
    else:
        return 1 + kolvo_elem(arr[1:])
    
def max_mas(arr, maximum):
    if arr == []:
        return maximum
    else:
        if arr[0] > maximum:
            maximum = arr[0]
        return max_mas(arr[1:], maximum)
    
n = [20, 1, 3, 5, 1, 1]
print(sum_elem(n))
print(kolvo_elem(n))
print(max_mas(n, n[0]))