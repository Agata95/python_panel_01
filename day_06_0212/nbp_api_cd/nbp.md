Pobierz listę kursów walut z zakresu dat:
2022-11-01 do 2022-11-11 i wyświetl na ekranie wartości kursu określonej waluty z tych dni w postaci listy.

```python

data_od = "2022-11-01"
data_do = "2022-11-11"
waluta = "CHF"

api_link = "http://api.nbp.pl/api/exchangerates/rates/{table}/{code}/{startDate}/{endDate}/"

lista_wartosci = []

# tu dalszy kod

# oczekiwany wynik:
print(f"Waluta {waluta} wynosi: {lista_wartosci}")

# np.:
# Waluta CHF wynosi: [4.784, 4.884, 4.184, 4.784, 4.884, 4.184, 4.784, 4.884, 4.184, 5.111 ]
```