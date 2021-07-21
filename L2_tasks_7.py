# Task 7

def sets_natural_numbers():
    """
    7. Напишите программу, доказывающую или проверяющую,
    что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
    где n - любое натуральное число.
    :return:
    """
    numbers = int(input('Введите любое натуральное число: '))
    sumNumb = 0
    for i in range(1, numbers + 1):
        sumNumb += i
    equality = numbers * (numbers + 1) // 2
    print(sumNumb)
    print(equality)


sets_natural_numbers()
