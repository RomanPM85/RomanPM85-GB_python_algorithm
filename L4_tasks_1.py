#Tasks 4.1
"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трёх уроков.
"""

import math
import timeit


def sieve_without_eratosthenes(i):
    """
    Функция поиска i-го простого числа,
    без использования алгоритма «Решето Эратосфена»
    :param i:
    :return:
    """

    lst_prime = [2]
    number = 3
    while len(lst_prime) < i:
        flag = True
        for j in lst_prime.copy():
            if number % j == 0:
                flag = False
                break
        if flag:
            lst_prime.append(number)
        number += 1
    return lst_prime[-1]


def sieve_eratosthenes(i):
    """
    Функция поиска i-го простого числа,
    используя алгоритм «Решето Эратосфена»
    :param i:
    :return:
    """

    i_max = prime_counting_function(i)
    lst_prime = [_ for _ in range(2, i_max)]

    for number in lst_prime:
        if lst_prime.index(number) <= number - 1:
            for j in range(2, len(lst_prime)):
                if number * j in lst_prime[number:]:
                    lst_prime.remove(number * j)
        else:
            break
    return lst_prime[i - 1]


def prime_counting_function(i):
    """
    Функция возвращает верхнюю границу отрезка на котором лежат
    i-e количество простых чисел. Функция основана на теореме о
    распределении простых чисел, она утверждает, что функция
    распределения простых чисел. Количество простых чисел на отрезке
    [1;n] растёт с увеличением n как n / ln(n).
    :param i:
    :return:
    """

    number_of_primes = 0
    number = 2
    while number_of_primes <= i:
        number_of_primes = number / math.log(number)
        number += 1
    return number


num_ex = 1
test_value = 1000

time1 = timeit.timeit(f'sieve_without_eratosthenes({test_value})',
                      setup='from __main__ import sieve_without_eratosthenes',
                      number=num_ex)

time2 = timeit.timeit(f'sieve_eratosthenes({test_value})',
                      setup='from __main__ import sieve_eratosthenes',
                      number=num_ex)

print(f'Программа без использования алгоритма «Решето Эратосфена» быстрее \
программы с использованием алгоритма «Решето Эратосфена» в \
{round(time2 / time1, 2)} раз')
"""
Программа без использования алгоритма «Решето Эратосфена» быстрее
программы с использованием алгоритма «Решето Эратосфена» в пределах  64.75 - 74,06 раза.
"""
