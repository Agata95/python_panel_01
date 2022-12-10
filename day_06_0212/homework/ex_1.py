from day_06_0212.homework.ex_1_utils import *

template_single_employee = {
    'name_and_surname': None,
    'department': None,
    'salary': 0,
}

employees_list = []
database = []

# todo:
#  zapisać dane do pliku i z pliku zczytywać,
#  może lepiej zrobić aby id było w templates i nadawało się automatycznie?


def company_structure():
    while True:
        print("""
            1 - Add new emplyee
            2 - Print info about emplyee
            3 - Print all employees list
            4 - Finanse and salary
            Q - Quit
            """)
        choice = input("Check one: ")

        if choice.upper() == 'Q':
            break
        elif choice == '1':
            new = add_new_emplyee(template_single_employee)
            add_to_list(employees_list, new, database)
            print("Employee added.")
        elif choice == '2':
            print_about_employee(database)
        elif choice == '3':
            print_all_employees(employees_list)


company_structure()
