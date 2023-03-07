# Test Driven Development w Python - 3h

TDD (Test-Driven Development) to metoda tworzenia oprogramowania, w której najpierw pisze się testy jednostkowe, a następnie implementuje się kod, który spełnia te testy. W Pythonie można korzystać z różnych bibliotek do testów jednostkowych, takich jak unittest czy pytest.

1. Napisz test jednostkowy dla kawałka kodu, który chcesz napisać. Upewnij się, że test jest odpowiednio specyficzny i przewiduje wszystkie możliwe scenariusze.
2. Uruchom test i upewnij się, że nie przechodzi on pomyślnie (powinien zwrócić błąd).
3. Napisz minimalną ilość kodu, która pozwoli na przejście testu.
4. Uruchom ponownie testy jednostkowe i upewnij się, że wszystkie przechodzą pomyślnie.
5. Refaktoryzuj kod, aby był czytelny i łatwy do utrzymania.
6. Powtórz kroki 1-5 dla kolejnych fragmentów kodu.


## Ważne jest, aby pisać testy jednostkowe dla małych, odizolowanych fragmentów kodu, a nie dla całego projektu naraz. Dzięki temu łatwiej jest zidentyfikować i naprawić błędy.

----

Zadanie lekcyjne:

* Projekt aplikacji, która :
  * klasa Ubezpieczony z 3 metodami: 
    - wpisz dane rodo (dane osobowe z szyfrowaniem)
    - podaj zliczony kapitał (na dzień aktualny)
    - podaj zarobki w roku X
  * słownik zawierający dane o ubezpieczonych
  * zapis do pliku w formacie pickle
  * odczyt z pliku w formacie pickle
  * przeglądanie danych
  * edycja danych
* testy jednostkowe z wykorzystaniem PyTest + fixtures + markers

Przeprowadzić proces wg metodologi TDD z refaktoryzacją kodu w kolejnych commitach/push.

Dodatkowo użyj modułu uuid https://docs.python.org/3/library/uuid.html i funkcji uuid5, np:
`uuid.uuid5(uuid.NAMESPACE_OID, "Adam Jurkiewicz")`

