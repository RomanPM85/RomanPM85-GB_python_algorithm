# Task 2

def even_odd_digits():
    """
    2. Посчитать четные и нечетные цифры введенного натурального числа.
    Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
    :return: 
    """
    numbers = int(input('Введите натуральное число: '))
    even = odd = 0
    while numbers > 0:
        if numbers % 2 == 0:
            even += 1
        else:
            odd += 1
        numbers = numbers // 10
    print("четных - %d, нечетных - %d" % (even, odd))


even_odd_digits()
