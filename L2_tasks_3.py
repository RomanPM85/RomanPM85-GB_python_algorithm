# Task 3

def reversNumbers():
    """
    3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
    Например, если введено число 3486, то надо вывести число 6843.
    :return:
    """
    numbers = int(input('Введите число: '))
    rev_num = 0
    while numbers > 0:
        rev_num = rev_num * 10 + numbers % 10
        numbers = numbers // 10
    print(rev_num)


reversNumbers()
