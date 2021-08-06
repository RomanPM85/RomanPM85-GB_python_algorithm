# Task 7

import random


def bubble_sort(lst):
    """
    1. Отсортируйте по убыванию методом "пузырька" одномерный
    целочисленный массив, заданный случайными числами на
    промежутке [-100; 100). Выведите на экран исходный и
    отсортированный массивы. Сортировка должна быть реализована
    в виде функции. По возможности доработайте алгоритм
    (сделайте его умнее).
    """
    n = 1

    while n < len(lst):
        count = 0

        for i in range(len(lst) - 1 - (n - 1)):

            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                count += 1

        if count == 0:
            break

        n += 1


SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 99
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print('Массив:', array, sep='\n')
bubble_sort(array)
print('После сортировки:', array, sep='\n')


def merge_sort(arr):
    """
    2. Отсортируйте по возрастанию методом слияния одномерный
    вещественный массив, заданный случайными числами на
    промежутке [0; 50). Выведите на экран исходный и
    отсортированный массивы.
    """

    def merge(fst, snd):
        res = []
        i, j = 0, 0

        while i < len(fst) and j < len(snd):

            if fst[i] < snd[j]:
                res.append(fst[i])
                i += 1

            else:
                res.append(snd[j])
                j += 1

        res.extend(fst[i:] if i < len(fst) else snd[j:])

        return res

    def div_half(lst):

        if len(lst) == 1:
            return lst

        elif len(lst) == 2:
            return lst if lst[0] <= lst[1] else lst[::-1]

        else:
            return merge(div_half(lst[:len(lst) // 2]), div_half(lst[len(lst) // 2:]))

    return div_half(arr)


SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 50
array = [random.uniform(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print('Массив:', array, sep='\n')
print('После сортировки:', merge_sort(array), sep='\n')


def median_search(lst, first, last):
    """
    3. Массив размером 2m + 1, где m – натуральное число, заполнен
    случайным образом. Найдите в массиве медиану.
    Медианой называется элемент ряда, делящий его на две
    равные части: в одной находятся элементы, которые
    не меньше медианы, в другой – не больше медианы.
    Задачу можно решить без сортировки исходного массива.
    Но если это слишком сложно, то используйте метод сортировки,
    который не рассматривался на уроках
    """

    lst = lst.copy()
    ind = len(lst) // 2

    if first >= last:
        return lst[ind]

    pillar = lst[ind]
    i = first
    j = last

    while i <= j:

        while lst[i] < pillar:
            i += 1

        while lst[j] > pillar:
            j -= 1

        if i <= j:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
            j -= 1

    if ind < i:
        lst[ind] = median_search(lst, first, j)

    elif j < ind:
        lst[ind] = median_search(lst, i, last)

    return lst[ind]


def merge_sort(arr):
    def merge(fst, snd):
        res = []
        i, j = 0, 0

        while i < len(fst) and j < len(snd):

            if fst[i] < snd[j]:
                res.append(fst[i])
                i += 1

            else:
                res.append(snd[j])
                j += 1

        res.extend(fst[i:] if i < len(fst) else snd[j:])

        return res

    def div_half(lst):

        if len(lst) == 1:
            return lst

        elif len(lst) == 2:
            return lst if lst[0] <= lst[1] else lst[::-1]

        else:
            return merge(div_half(lst[:len(lst) // 2]), div_half(lst[len(lst) // 2:]))

    return div_half(arr)


MIN_ITEM = 0
MAX_ITEM = 50
MIN_SIZE = 5
MAX_SIZE = 10

m = random.randint(MIN_SIZE, MAX_SIZE)
size = 2 * m + 1

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(size)]

print(f'Сгенерирован массив из 2*{m}+1 = {size}  элементов:', array, sep='\n')

median = median_search(array, 0, len(array) - 1)
print(f'Медиана: {median}')
# print(array, '\n')

print('Отсортированный массив: ', merge_sort(array), sep='\n')
if median == merge_sort(array)[len(array) // 2]:
    print('\nВерно')
else:
    print('\nОшибка!!!')
