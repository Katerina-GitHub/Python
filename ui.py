from dataProvider import get_person
from logger import write_txt, write_csv, read_contact


def click():
    print('1.Add a new contact\n2.Show phonebook')
    mode = int(input())
    if mode == 1:
        a = get_person()
        write_txt(a)
        write_csv(a)
    elif mode == 2:
        print(read_contact())
    else:
        print('Enter correct data')
