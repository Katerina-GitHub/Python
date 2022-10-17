day = int(input('Введите день недели: '))
if day > 7 or day < 1:
    print('Неккоректный ввод')
elif day == 6 or day == 7:
    print("Ура-ура выходные!")
else:
    print("Сегодня рабочий день!")