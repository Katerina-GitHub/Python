from studentsData import save_database, load_database
from students import check_rate
from teachers import rate, add_students


def brain_tank():
    load_database()
    match input('If you a teacher, press 1, a student- press 2: '):
        case '1':
            flag = 1
            while flag == 1:
                action = input(
                    'To place a new student press 1,   evaluate: press 2, to exit press 0:\n Press:')
                if action == '1':
                    add_students()
                elif action == '2':
                    rate()
                elif action == '0':
                    flag = 0
            else:
                save_database()
        case '2':
            flag = 1
            while flag == 1:
                family_name = input(
                    'Enter family name or press 0 to exit\n Press: ')
                if family_name == '0':
                    flag = 0
                else:
                    check_rate(family_name)
