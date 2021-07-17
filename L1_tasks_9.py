# Task 9

def average_number():
    """
     Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
    :return:
    """
    print('Введите три числа: ')
    a = int(input('Первое число: '))
    b = int(input('Второе число: '))
    c = int(input('Третье число: '))
    messages = "Среднее число: "

    if b < a < c or c < a < b:
        print(f'{messages}{a}')
    elif a < b < c or c < b < a:
        print(f'{messages}{b}')
    else:
        print(f'{messages}{c}')


average_number()
