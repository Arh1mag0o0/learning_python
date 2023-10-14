# функция принимает список значений и искомоме значение, возвращает индекс значение, если такого значения нет возвращает None
def binary_searth(list1, item):
    low = 0
    high = len(list1)-1
    
    while low <= high:
        mid = (low + high) // 2
        guess = list1[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1, 3, 5, 10, 25]

print(binary_searth(my_list, 5))
print(binary_searth(my_list, 2))