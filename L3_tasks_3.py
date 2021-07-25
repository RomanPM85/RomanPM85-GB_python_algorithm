# Task 3
from random import random


def swap_elem_array():
    """
    3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
    :return:
    """

    N = int(input('Введите количество элементов в массиве: '))
    arr = [0] * N
    for i in range(N):
        arr[i] = int(random() * 100)
        print(arr[i], end=' ')
    print()

    minElem = min(arr)
    maxElem = max(arr)
    imn = arr.index(minElem)
    imx = arr.index(maxElem)
    arr[imn], arr[imx] = arr[imx], arr[imn]

    for i in range(N):
        print(arr[i], end=' ')
    print()


swap_elem_array()
