1. Wykonaj testy analogiczne do `day_11_2812_TEST/tests_production/test_class_import.py`, lecz z wykorzystaniem `pytest`. Użyj 3 danych wejściowych, a więc 3 funkcje sprawdzające

2. Wykonaj jak powyżej, ale z wykorzystaniem `@fixtures` - zrefaktoryzowanie kodu.

3. Do klasy Person dodaj wywołanie wyjątku `TooOldPerson` dla próby stworzenia osoby urodzonej przed 1900 rokiem; opisz wyjątek w pliku `exceptions.py` i sprawdź, czy podczas tworzenia obiektu zostaje on usunięty z pamięci (`NameError` dla `dir(obiekt)`)

4. Wykonaj testy analogiczne do `day_11_2812_TEST/tests_production/test_class_import.py`, lecz z wykorzystaniem `pytest`. Użyj `fixtures` do zbudowania 3 danych wejściowych ...

5. Obuduj te testy markerami i sprawdź różne sposoby wywoływania
