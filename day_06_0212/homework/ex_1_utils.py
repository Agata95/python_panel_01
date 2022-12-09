import json


def add_new_emplyee(template: dict) -> dict:
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
