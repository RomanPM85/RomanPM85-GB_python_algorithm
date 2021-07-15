# Task 4
import random


def user_random():
    '''
    4. Написать программу, которая генерирует в указанных пользователем границах:
    случайное целое число;
    случайное вещественное число;
    случайный символ.
    :return:
    '''

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


user_random()
