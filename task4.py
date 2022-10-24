from random import randint

k = int(input('Введите степень '))
for i in range(k, 0, -1):
    rate = randint(1, 100)
    if rate == 1:
        rate = " "
    else:
        if i != 1:
            rate = f'{rate}*x^{i} +'
        else:
            rate = f"{rate}*x +"
    print(rate, end='')
print(f'{randint(1, 100)} = 0')
