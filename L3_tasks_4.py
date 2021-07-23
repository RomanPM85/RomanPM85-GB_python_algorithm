# Task 4
from random import random


def frequent_elem_array():
    """
    4. Определить, какое число в массиве встречается чаще всего.
    :return:
    """
    N = int(input('Введите количество элементов в массиве: '))
    arr = [0] * N
    for i in range(N):
        arr[i] = int(random() * 20)
    print(arr)

    num = arr[0]
    max_frq = 1
    for i in range(N - 1):
        frq = 1
        for k in range(i + 1, N):
            if arr[i] == arr[k]:
                frq += 1
        if frq > max_frq:
            max_frq = frq
            num = arr[i]

    if max_frq > 1:
        print(max_frq, 'раз(а) встречается число', num)
    else:
        print('Все элементы уникальны')


frequent_elem_array()
