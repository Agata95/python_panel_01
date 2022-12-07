import requests

# daty od tydzień temu do dziś automatycznie.

data_od = "2022-11-01"
data_do = "2022-11-11"
waluta = "CHF"

# tu dalszy kod

api_link = f"http://api.nbp.pl/api/exchangerates/rates/A/{waluta}/{data_od}/{data_do}/"
r_api = requests.get(api_link)
odczyt = r_api.json()
odczyt_lista = odczyt['rates']

# oczekiwany wynik:
print(f"Waluta {waluta} wynosi: {odczyt_lista}")