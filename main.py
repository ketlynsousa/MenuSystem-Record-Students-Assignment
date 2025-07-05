from modules.interface import *
from modules.datas import *

data_file = 'students_record_file.py'

while True:
    register_list = list()
    heading("STUDENTS RECORD SYSTEM")
    menu_options = menu(['RECORD NEW STUDENT', 'CONSULT REGISTRATION', 'FILTER STUDENTS', 'GENERAL STATISTICS', 'EXIT THE SYSTEM'])

    if menu_options == 1:
        heading('RECORD NEW STUDENT')
        name = str(input('Enter the name: ')).strip().title()
        age = readInt("Enter the age: ")
        while True:
            gender = str(input("Enter gender: [F/M] ")).upper().strip()
            if gender in ('F', 'M'):
                break
            else:
                print("Invalid option. ", end='')
        average_grade = readFloat("Enter final average grade: ")
    elif menu_options == 2:
        heading('opt2')
    elif menu_options == 3:
        heading('opt3')
    elif menu_options == 4:
        heading('opt4')
    elif menu_options == 5:
        heading('SYSTEM CLOSED...')
        break
    else:
        print(f"ERROR! Enter a valid option.")
