# Task 9

def max_sum_natural():
    """
    9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
    Вывести на экран это число и сумму его цифр.
    :return:
    """
    print('Для выхода из программы наберите 0 и нажмите Enter')
    n = int(input('Введите число: '))
    max_s = 0
    max_m = 0
    while n != 0:
        m = n
        s = 0
        while n > 0:
            s += n % 10
            n //= 10
        if s > max_s:
            max_s = s
            max_m = m
        n = int(input('Введите следующее число или наберите 0, чтобы выйти из программы и получить сумму: '))
    print('Число', max_m, 'имеет максимальную сумму цифр:', max_s)


max_sum_natural()
