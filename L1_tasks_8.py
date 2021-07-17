


def leap_year():
    """
    Определить, является ли год, который ввел пользователем, високосным или невисокосным.
    :return:
    """
    y = int(input("Введите год: "))
    messageNormal = 'Год обычный'
    messageLeapYear = 'Год високосный'
    if y % 4 != 0:
        print(messageNormal)
    elif y % 100 == 0:
        if y % 400 == 0:
            print(messageLeapYear)
        else:
            print(messageNormal)
    else:
        print(messageLeapYear)


leap_year()
