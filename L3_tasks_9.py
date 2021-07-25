# Task 9
from random import random


def max_min_elem_in_matrix():
    """
    9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
    :return:
    """
    M = 10
    N = 5
    a = []
    for i in range(N):
        b = []
        for j in range(M):
            n = int(random() * 200)
            b.append(n)
            print('%5d' % n, end='')
        a.append(b)
        print()

    mx = -1
    for j in range(M):
        mn = 200
        for i in range(N):
            if a[i][j] < mn:
                mn = a[i][j]
        if mn > mx:
            mx = mn
    print("Максимальный среди минимальных: ", mx)


max_min_elem_in_matrix()
