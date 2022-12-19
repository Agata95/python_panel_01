"""
Aplikacja główna
"""
from funkcje_pomocnicze import *

insured = {
    'number': 0,
    'names': [],
}

insured_person = {
    'name_and_surname': None,
    'phone_no': None,
    'premium': 0,
}

# todo: do zrobienia podpunkty 1 i 2
while True:
    print("""
    1 - Open file
    2 - Print all insured
    3 - Add new insured
    4 - Save file
    Q - Quit
    """)
    choice = input("Check one: ")
    if choice.upper() == 'Q':
        break

    elif choice == '3':
        data_insured = add_insured(insured_person)

    elif choice == '4':
        result = save_file(insured, 'insured_data.dat')
        if result:
            print("Database was saved.")
