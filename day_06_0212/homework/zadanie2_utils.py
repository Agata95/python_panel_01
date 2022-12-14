import json


def add_new_employee(template: dict) -> dict:
    print("Provide information about new employee:")

    new_dict = {}
    for any_key in template:
        new_value = input(f"{any_key}: ")
        new_dict[any_key] = new_value

    return new_dict


def add_to_list(employees_list: list, new_employee: dict, database: list):
    index = len(employees_list) + 1
    if len(employees_list) == 0:
        new_dict = {'id': 1, 'name': new_employee['name_and_surname']}
        database_dict = {'id': 1, 'data': new_employee}
    else:
        new_dict = {'id': index, 'name': new_employee['name_and_surname']}
        database_dict = {'id': index, 'data': new_employee}

    employees_list.append(new_dict)
    database.append(database_dict)

    return employees_list, database


def check_number_in_list(number: str, database: list) -> bool:
    try:
        for el in database:
            if el['id'] == int(number):
                return True

    except Exception as ex:
        print(ex)

    return False


def print_employee(number: str, database: list):
    employee = {}
    for el in database:
        if el['id'] == int(number):
            employee = el['data']

    print(json.dumps(employee, indent=4))


def print_all_employee_numbers(database: list):
    numbers_list = [el['id'] for el in database]
    print(numbers_list)


def print_about_employee(database: list):
    number = input("Enter emplyee's number: ")
    if check_number_in_list(number, database):
        print_employee(number, database)
    else:
        print("Wrong number. Please put the right number from list below:")
        print_all_employee_numbers(database)


def print_all_employee(database: list, employees: dict):
    for el in database:
        employees.update({el['id']: el['data']['name_and_surname']})

    print(json.dumps(employees, indent=4))


def salary(database: list):
    departments = list(dict.fromkeys([(el['data']['department']).upper() for el in database]))
    print("Enter 'all' or 'name of department' to print total sum of salary employees all or emplayees of department.")
    print('Departments:', departments)
    value = input()
    salary_all = 0.0
    dep = ''

    if value.upper() == 'ALL':
        dep = 'all'
        for el in database:
            salary_all += float(el['data']['salary'])
    elif value.upper() in departments:
        dep = value.upper()
        for el in database:
            if (el['data']['department']).upper() == dep:
                salary_all += float(el['data']['salary'])

    return salary_all, dep
