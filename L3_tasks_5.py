# Task 5
from random import random


def max_negative_elem():
    """
    5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
    :return:
    """
    N = int(input('Введите количество элементов в массиве: '))
    arr = []
    for i in range(N):
        arr.append(int(random() * 100) - 50)
    print(arr)

    i = 0
    index = -1
    while i < N:
        if arr[i] < 0 and index == -1:
            index = i
        elif 0 > arr[i] > arr[index]:
            index = i
        i += 1

    print(index + 1, ':', arr[index])


max_negative_elem()
