import requests
from datetime import datetime, timedelta

# daty od tydzień temu do dziś automatycznie.

today_is = datetime.today()
waluta = "CHF"

api_link = f"http://api.nbp.pl/api/exchangerates/rates/A/{waluta}/{today_is - timedelta(7)}/{today_is.date()}/"

r_api = requests.get(api_link)
odczyt = r_api.json()
odczyt_lista = odczyt['rates']

# oczekiwany wynik:
print(f"Waluta {waluta} wynosi: {odczyt_lista}")
