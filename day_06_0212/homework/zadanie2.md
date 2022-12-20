Napisz program, który będzie zawierał
słownik o strukturze:

```python
dane_pracownika = {
    'imie_nazwisko' : 'value',
    'dzial_firmy' : 'nazwa_dzialu',
    'pensja_miesieczna': 0,
    }
```

oraz listę pracowników zmienna ```<list>```.

Program musi mieć funkcje:
- dodanie nowego pracownika do listy pracownikow - bez parametrów, wszystkie operacje wewnątrz funkcji
- pokazanie wszystkich danych o pracowniku - funkcja z parametrem numer pracownika, równy indeksowi listy pracowników
- koszty pracownicze - funkcja ma miec 2 parametry:
  - 1szy o wartości domyślnej "all" - wtedy pokaże sumę pensji wszystkich pracowników; a jeśli wartość tego parametru będzie inna,
    wówczas ma zliczać sumę pensji tylko dla pracowników danego działu
  - 2gi o wartości domyślnej 12 - ilość miesięcy, dla których liczona jest wartość pensji pracowniczych dla osób spełniających warunek parametru 1