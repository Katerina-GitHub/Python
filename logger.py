from dataProvider import get_person as gp


def read_contact():
    with open('phonebook.csv', 'r', encoding='utf-8') as data:
        return data.read()


def write_csv(gp):
    file = 'phonebook.csv'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(
            f'Фамилия: {gp[0]};Имя: {gp[1]};Телефон: {gp[2]};Описание: {gp[3]}\n')


def write_txt(gp):
    file = 'log.txt'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(
            f'Фамилия: {gp[0]}\nИмя: {gp[1]}\nТелефон: {gp[2]}\nОписание: {gp[3]}\n\n')
