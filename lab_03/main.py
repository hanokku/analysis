def gnome_sort(array):
    i = 1
    while i < len(array):
        if (array[i - 1] <= array[i]):
            i = i + 1
        else:
            tmp = array[i]
            array[i] = array[i - 1]
            array[i - 1] = tmp
            i = i - 1
            if (i == 0):
                i = 1
    return array


def insert_sort(array):
    for i in range(len(array)):
        j = i - 1
        tmp = array[i]
        while array[j] > tmp and j >= 0:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = tmp
    return array


def bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def print_arr(string, arr):
    print(string, end = ': ')
    for i in range(len(arr)):
        print(arr[i], end = ' ')
    print()
        

if __name__ == '__main__':
    a = []
    length = int(input('Введите длину массива: '))
    for i in range(length):
        num = int(input('Введите {0}-й элемент массива: '.format(i)))
        a.append(num)
    b = a
    c = a
    print()
    print_arr('Результат сортировки гномьей сортировкой: ', gnome_sort(a))
    print_arr('Результат сортировки сортировкой вставками: ', insert_sort(b))
    print_arr('Результат сортировки сортировкой пузырьком: ', bubble_sort(c))
