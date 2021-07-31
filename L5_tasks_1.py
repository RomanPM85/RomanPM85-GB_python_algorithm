"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести
наименования предприятий, чья прибыль ниже среднего.
Примечание: для решения задач попробуйте применить какую-нибудь коллекцию из
модуля collections
"""

import collections


def sum_tuple(numbers):
    """
    tuple --> sum
    :param numbers:
    :return:
    """

    total_sum = 0
    for sum_q in numbers:
        total_sum += sum_q
        return total_sum


Enterprise = collections.namedtuple('Предприятие', ['quarter_1', 'quarter_2', 'quarter_3', 'quarter_4'])

base_enterprise = {}

quantity = None
while True:
    quantity = input('Количество предприятий: ')
    if quantity.isdigit():
        print('Ok')
        quantity = int(quantity)
        break
    else:
        print('Введите количество предприятий цифрой!')


for i in range(quantity):
    name = input(str(i + 1) + '-е предприятие: ')
    profit_q1 = int(input('Прибыль за 1-й квартал: '))
    profit_q2 = int(input('Прибыль за 2-й квартал: '))
    profit_q3 = int(input('Прибыль за 3-й квартал: '))
    profit_q4 = int(input('Прибыль за 4-й квартал: '))
    base_enterprise[name] = Enterprise(
        quarter_1=profit_q1,
        quarter_2=profit_q2,
        quarter_3=profit_q3,
        quarter_4=profit_q4
    )

total_profit = ()

for name, profit in base_enterprise.items():
    print(f'Предприятие: {name} прибыль за год - {sum(profit)}')
    total_profit += profit

avg_profit_total = sum(total_profit) / len(base_enterprise)
print(f'Средняя прибыль за год для всех предприятий {avg_profit_total}')

print('Предприятия, у которых прибыль выше среднего:')

for name, profit in base_enterprise.items():
    if sum(profit) > avg_profit_total:
        print(f'{name} - {sum(profit)}')

print('Предприятия, у которых прибыль ниже среднего:')
for name, profit in base_enterprise.items():
    if sum(profit) < avg_profit_total:
        print(f'{name} - {sum(profit)}')
