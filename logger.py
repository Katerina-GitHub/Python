from ui import get_person as gp

person = gp()


def write_txt():
    file = 'log.txt'
    with open(file, 'w') as data:
        data.write(
            f'Фамилия: {person[0]};Имя: {person[1]};Телефон: {person[2]};Описание: {person[3]}')
