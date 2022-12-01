import json
import os


def set_students(data_list):
    student_database[data_list[0]] = data_list[1:], {}


def set_rates(family_name, lesson, grade):
    if student_database.get(family_name) is None:
        print('There is no {family_name}')
        print(student_database)
    else:
        if lesson in student_database[family_name][1]:
            student_database[family_name][1][lesson].extend(grade)
        else:
            student_database[family_name][1][lesson] = grade


def get_students(family_name_student):
    if student_database.get(family_name_student) is None:
        print('There is no {family_name_student}')
    else:
        data = student_database[family_name_student]
        print(f'{family_name_student}{",".join(data[0])}:')
        print(*[f'{key}: {",".join(value)}' for key,
              value in data[1].items()], sep='\n')


def save_database():
    json.dump(student_database, open('student_database.json', 'w'))


def load_database():
    global student_database
    if os.stat('student_database.json').st_size == 0:
        student_database = {}
    else:
        student_database = json.load(open('student_database.json'))
