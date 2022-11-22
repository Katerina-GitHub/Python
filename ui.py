def get_person():
    person = []
    sirname = input('Введите фамилию: ')
    person.append(sirname)
    name = input('Введите имя: ')
    person.append(name)
    phone_number = input('Введите номер телефона: ')
    phone_number = int(phone_number)
    person.append(phone_number)
    description = input('Введите описание: ')
    person.append(description)
    return
