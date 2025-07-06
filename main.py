from modules.interface import *
from modules.datas import *
from students_table_display import *

students_under18 = list()
females_students = list()
students_grade7 = list()
register_list = list()
total_grades = list()
females_grade_7over = list()

# while loop for main condition of the menu and each condition with their sub conditions and loops when required.
while True:
    heading("STUDENTS RECORD SYSTEM")
    menu_options = menu(['RECORD NEW STUDENT', 'CONSULT REGISTRATION', 'FILTER STUDENTS', 'GENERAL STATISTICS', 'EXIT THE SYSTEM'])

    # Registering section and appending data to register_list
    if menu_options == 1:
        heading('RECORD NEW STUDENT')

        name = str(input('Enter the name: ')).strip().title()
        while True:
            try:
                age = readInt("Enter the age: ")
                if age <= 0:
                    raise ValueError
                break
            except ValueError:
                print(f"{use_colours('red')}ERROR! Enter a valid age. {use_colours('clean')}")

        while True:
            gender = str(input("Enter gender: [F/M] ")).upper().strip()
            if gender in ('F', 'M'):
                break
            else:
                print(f"{use_colours('red')}Invalid option. {use_colours('clean')}", end='')
        average_grade = readFloat("Enter final average grade: ")
        register_list.append([name, age, gender, average_grade])

        # Conditions for appending for sub lists for option 3 or 4 of the menu
        if gender == 'F':
            females_students.append(name)
        if average_grade >= 7:
            students_grade7.append({'Name': name, 'Average': average_grade})
        if age < 18:
            students_under18.append({'Name': name, 'Age': age})
        if gender == 'F' and average_grade >=7:
            females_grade_7over.append(name)
        total_grades.append(average_grade)

    # Option to display the table of students registered with function showTable()
    elif menu_options == 2:
        heading('CONSULTING RECORDS')
        showTable(register_list)

    # Option to filter students with menu and conditions to display each section
    elif menu_options == 3:
        while True:
            heading('FILTERING RECORDS')
            menu_option3 = menu(['DISPLAY ONLY GIRLS', 'DISPLAY AVERAGE 7 OR OVER', 'STUDENTS UNDER 18yo'])

            if menu_option3 == 1:
                heading2("List of girls registered")
                for f in females_students:
                    print(f"{use_colours('magenta')}- {f}{use_colours('clean')}")
                break

            elif menu_option3 == 2:
                heading2("List of students with grade 7 or over")
                for s in students_grade7:
                    print(f"{use_colours('magenta')}{s}{use_colours('clean')}")
                break

            elif menu_option3 == 3:
                heading2("Students under 18 years old")
                for s in students_under18:
                    print(f"{use_colours('magenta')}{s}{use_colours('clean')}")
                break

            else:
                print(f"{use_colours('red')}ERROR! Enter a valid option.{use_colours('clean')}")
                continue

    # Option to display general statistics of students registered
    elif menu_options == 4:
        heading("GENERAL STATISTICS")
        print(f"{use_colours('magenta')}- In total {len(register_list)} students were registered.{use_colours('clean')}")

        average_total_grades = sum(total_grades) / len(total_grades)
        print(f"{use_colours('magenta')}- Average of all grades registered is {average_total_grades:.1f}.{use_colours('clean')}")

        print(f"{use_colours('magenta')}- A total of {len(students_grade7)} students had grade 7 or over.{use_colours('clean')}")

        print(f"{use_colours('magenta')}- A total of {len(females_grade_7over)} girls had grade 7 or over.{use_colours('clean')}")

    # Option to close the system
    elif menu_options == 5:
        heading('SYSTEM CLOSED...')
        break
    # Option to error in the main menu
    else:
        print(f"{use_colours('red')}ERROR! Enter a valid option.{use_colours('clean')}")
