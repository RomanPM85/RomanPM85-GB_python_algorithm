""" Task 6. Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков. Проанализировать
результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
комментариев к коду. Также укажите в комментариях версию Python и разрядность
вашей ОС. """

import sys
import random

"""
(sysname='Linux', nodename='Roman', release='5.11.0-25-generic', version='#27~20.04.1-Ubuntu machine='x86_64'
Python 3.8.10
"""


# Task 1
def get_sum():
    """
    Найти сумму цифр трехзначного числа, которое вводит пользователь.
    :return:
    """
    while True:
        print(f'Для выхода из программы наберите stop')
        numbers_User = input('или введите трехзначное число: ')
        if numbers_User == 'stop':
            break
        else:
            if numbers_User[0] != '-':
                if numbers_User.isdigit():
                    if 3 == len(numbers_User):
                        sumNumbers = 0
                        for x in numbers_User:
                            sumNumbers = sumNumbers + int(x)
                        print(f'Сумма чисел равна: {sumNumbers} ')
                    else:
                        print(f'Необходимо только 3х значное число!!!')
                else:
                    print(f'Ввод букв запрещен, вводить необходимо только 3х значное число!!!')
            else:
                if numbers_User[0] == '-':
                    nowNumbers = numbers_User[1:4]
                    print(len(nowNumbers))
                    if 3 == len(nowNumbers):
                        sumNumbers = int(nowNumbers[0]) * (-1)
                        for x in nowNumbers[1:3]:
                            sumNumbers = sumNumbers + int(x)
                        print(f'Сумма чисел равна: {sumNumbers} ')
                    else:
                        print(f'Необходимо только 3х значное число!!!')
                else:
                    print(f'Необходимо только 3х значное число!!!')


# Task 3

def equationFun():
    """
    3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b, проходящей через
    эти точки.
    :return:
    """
    print("Координаты точки A(x1;y1):")
    x1 = float(input("\tx1 = "))
    y1 = float(input("\ty1 = "))

    print("Координаты точки B(x2;y2):")
    x2 = float(input("\tx2 = "))
    y2 = float(input("\ty2 = "))

    print("Уравнение прямой, проходящей через эти точки:")
    k = (y1 - y2) / (x1 - x2)
    b = y2 - k * x2
    print(" y = %.2f*x + %.2f" % (k, b))


# equationFun()


# Task 4

def user_random():
    """
    4. Написать программу, которая генерирует в указанных пользователем границах:
    случайное целое число;
    случайное вещественное число;
    случайный символ.
    :return:
    """

    def rangeInt():
        user_rangeInt = (int(input('Введите целое число нижней границы диапазона от: ')),
                         int(input('и верхнюю границу диапазона до: ')))
        output_randomInt = random.randint(user_rangeInt[0], user_rangeInt[1])
        print(f'Ваше случайное целое число: {output_randomInt} в границах от {user_rangeInt[0]} до {user_rangeInt[1]}')

    rangeInt()

    def rangeFloat():
        user_rangeFloat = (float(input('Введите  вещественное число нижней границы диапазона от: ')),
                           float(input('и верхнюю границу диапазона до: ')))
        output_randomFloat = random.uniform(user_rangeFloat[0], user_rangeFloat[1])
        print(f'Ваше случайное вещественное число: {output_randomFloat} в границах от {user_rangeFloat[0]} '
              f'до {user_rangeFloat[1]}')

    rangeFloat()

    def rangeStr():
        user_rangeStr = (ord(input('Введите букву нижней границы диапазона от: ')),
                         ord(input(' и букву верхней границы диапазона до: ')))
        # print(user_rangeStr)
        output_randomInt = random.randint(user_rangeStr[0], user_rangeStr[1])
        # print(output_randomInt)
        # print(chr(output_randomInt))
        print(f'случайный символ из алфавита: {chr(output_randomInt)} в границах от {chr(user_rangeStr[0])} '
              f'до {chr(user_rangeStr[1])}')

    rangeStr()


print(f'Объем памяти после вызова программы из домашнего задания к уроку 1 составляет:'
      f' {sys.getsizeof(get_sum())} байта')
#  Объем памяти после вызова программы из домашнего задания к уроку 1 составляет: 16 байта
print(f'Объем памяти после вызова программы из домашнего задания к уроку 1 составляет:'
      f' {sys.getsizeof(get_sum)} байта')
#  Объем памяти после вызова программы из домашнего задания к уроку 1 составляет: 136 байта


print(f'Объем памяти после вызова программы из домашнего задания к уроку 3 составляет: '
      f'{sys.getsizeof(equationFun())} байта')
#  Объем памяти после вызова программы из домашнего задания к уроку 3 составляет: 16 байта
print(f'Объем памяти после вызова программы из домашнего задания к уроку 3 составляет: '
      f'{sys.getsizeof(equationFun)} байта')
#  Объем памяти после вызова программы из домашнего задания к уроку 3 составляет: 136 байта


print(f'Объем памяти после вызова программы из домашнего задания к уроку 4 составляет: '
      f'{sys.getsizeof(user_random())} байта')
#  Объем памяти после вызова программы из домашнего задания к уроку 4 составляет: 16 байта
print(f'Объем памяти функция программы из домашнего задания к уроку 4 составляет: '
      f'{sys.getsizeof(user_random)} байта')
#  Объем памяти после вызова программы из домашнего задания к уроку 4 составляет: 136 байта

sum_size = 0
sum_size += sys.getsizeof(get_sum)
sum_size += sys.getsizeof(equationFun)
sum_size += sys.getsizeof(user_random)

print(f'Функции из 3-х заданий суммарно занимают {sum_size}, байта')
# Функции из 3-х заданий суммарно занимают 408, байта
