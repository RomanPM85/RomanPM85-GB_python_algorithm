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
                    print(f'Ввод букв запрещен!!! вводить необходимо только 3х значное число!!!')
            elif numbers_User[0] == '-':
                nowNumbers = numbers_User[1:]
                if nowNumbers.isdigit():
                    if 3 == len(nowNumbers):
                        sumNumbers = 0
                        for x in nowNumbers[1:]:
                            """
                            Вариант, если пользователь вводит отрицательное число, тогда первое число
                            берем со знаком "-" и складываем с двумя положительными числами идущие после него.
                            """
                            sumNumbers = sumNumbers + int(x)
                        totalSum = int(nowNumbers[:1]) * (-1) + sumNumbers
                        print(f'Сумма чисел равна: {totalSum} ')
                    else:
                        print(f'Необходимо только 3х значное число!!!')
                else:
                    print(f'Ввод букв запрещен!!! вводить необходимо только 3х значное число!!!')
            else:
                break


def get_multiplication():
    """
    Найти  произведение цифр трехзначного числа, которое вводит пользователь.
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
                        multiplication = 1
                        for x in numbers_User:
                            multiplication = multiplication * int(x)
                        print(f'Произведение чисел равно: {multiplication} ')
                    else:
                        print(f'Необходимо только 3х значное число!!!')
                else:
                    print(f'Ввод букв запрещен, вводить необходимо только 3х значное число!!!')
            else:
                if numbers_User[0] == '-':
                    nowNumbers = numbers_User[1:4]
                    if 3 == len(nowNumbers):
                        multiplication = int(nowNumbers[0]) * (-1)
                        for x in nowNumbers[1:3]:
                            multiplication = multiplication * int(x)
                        print(f'Произведение чисел равно: {multiplication} ')
                    else:
                        print(f'Необходимо только 3х значное число!!!')
                else:
                    print(f'Необходимо только 3х значное число!!!')


get_sum()
# get_multiplication()
