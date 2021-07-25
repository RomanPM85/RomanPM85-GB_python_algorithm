# Task 1

def multiplicity_range():
    """
    1. В диапазоне натуральных чисел от 2 до 99 определить,
    сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
    :return:
    """
    a = [0] * 8
    for i in range(2, 100):
        for x in range(2, 10):
            if i % x == 0:
                a[x - 2] += 1
    i = 0
    while i < len(a):
        print(i + 2, ' - ', a[i])
        i += 1


multiplicity_range()
