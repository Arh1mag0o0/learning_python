# Сортировка выбором первая функция находит наименьший элемент входного массива, вторая переписывает его в новый массив через pop и вызывает последовательно первую, вторая возвращает отсортированный массив

def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print(selectionSort([3, 1, 5, 12, 34, 32]))
