"""
Aplikacja główna
"""
from funkcje_pomocnicze import *

ubezpieczeni = {
    "ilosc": 0,
    "nasi_milusinscy": [],
}

jeden_ubezpieczony = {
    "imie_nazwisko": None,
    "nr_telefonu": None,
    "skladka": 0,
}

while True:
    print(
        """
    1 - Odczyt danych z pliku
    2 - Pokaż ubezpieczonych
    3 - Dodaj ubepieczonego
    4 - Zapis pliku
    Q - Koniec pracy
    """
    )
    wybor = input("Podaj nr opcji:")
    if wybor.upper() == "Q":
        break

    if wybor == "4":
        wynik = zapis_pliku(ubezpieczeni, "baza.dat")
        if wynik:
            print("Baza zapisana.")

    if wybor == "3":
        dane_ubezpieczonego = dodaj_ubezpieczonego(jeden_ubezpieczony)
