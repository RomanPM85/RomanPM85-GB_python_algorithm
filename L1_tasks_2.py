# Task 2

def bitwiseOperations():
    """
    2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
    Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака. Объяснить полученный результат.
    :return:
    """
    binMessege = 'а в бинарном представлении будет '
    shiftMessege = 'Битовый сдвиг числа 5 на два знака '
    bitwiseNumbers = (5, 6)
    shiftRight = bitwiseNumbers[0] >> 2
    shiftLeft = bitwiseNumbers[0] << 2
    print(f'{shiftMessege} вправо будет {shiftRight}, {binMessege} {bin(shiftRight)}; \n{shiftMessege} влево '
          f'будет {shiftLeft}, {binMessege}{bin(shiftLeft)}')
    print('Побитовые операторы предназначены для работы с данными в битовом (двоичном) формате.'
          'Побитовый сдвиг, значение операнда "сдвигается" влево или вправо на количество бит указанных в операнде.')
    bitAnd = bitwiseNumbers[0] & bitwiseNumbers[1]
    print(f'Логические побитовые операции «И», над {bitwiseNumbers[0]} и {bitwiseNumbers[1]}, будет  {bitAnd};'
          f' при операции «ИЛИ», над {bitwiseNumbers[0]} и {bitwiseNumbers[1]}, будет  {bitAnd};')
    print('Логический оператор "И". Условие будет истинным если оба операнда истина.\n'
          'Логический оператор "ИЛИ". Если хотя бы один из операндов истинный, то и все выражение будет истинным.')


bitwiseOperations()
