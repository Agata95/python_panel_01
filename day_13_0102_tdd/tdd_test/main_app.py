from tdd_functions.class_insured import Insured
from tdd_functions.edit_data import *

"""
Główna aplikacja:
 * klasa Ubezpieczony z 3 metodami:
    - wpisz dane rodo (dane osobowe z szyfrowaniem)
    - podaj zliczony kapitał (na dzień aktualny)
    - podaj zarobki w roku X
  * słownik zawierający dane o ubezpieczonych
  * zapis do pliku w formacie pickle
  * odczyt z pliku w formacie pickle
  * przeglądanie danych
  * edycja danych
"""

insured = {}

while True:
    print("""MENU:
    1 - Add insured
    2 - Enter capital
    3 - Enter earnings
    4 - Save to file
    5 - Write from file
    6 - Viewing data
    7 - Edit data
    Q - QUIT
        """)
    choice = input("Give an option: ")
    if choice.upper() == 'Q':
        break

    print(f"{choice=}")
