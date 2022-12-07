import requests
import json
from icecream import ic

table = "A"

table_api = f'http://api.nbp.pl/api/exchangerates/tables/{table}/'

r_api = requests.get(table_api)
ic(requests.get(table_api))
print(r_api)
print('Koniec.')