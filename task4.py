q = int(input('Задайте номер четверти: '))
if q < 1 or q > 4:
    print('Невернный ввод')
elif q == 1:
    print('x > 0 и y > 0')
elif q == 2:
    print('x < 0 и y > 0')
elif q == 3:
    print('x < 0 и y < 0')
elif q == 4:
    print('x > 0 и y < 0')
