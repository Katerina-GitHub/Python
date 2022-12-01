from studentsData import set_students, set_rates


def add_students():
    student_data = input(
        'Enter student data using "," separator: Family name, name, class ').split(',')
    set_students(student_data)


def rate():
    family_name = input('Enter student family name: ')
    lesson = input('Enter lesson: ')
    grade = input('Enter grade: ')
    set_rates(family_name, lesson, grade)
