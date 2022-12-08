import requests
import json
from icecream import ic

table = "A"
table_api = f"http://api.nbp.pl/api/exchangerates/tables/{table}/"

# funkcja get
r_api = requests.get(table_api)
ic(requests.get(table_api))

###
# Wyświetlanie funkcji content z odpowiedzi strony api
###

# w bitach, bez polskich znaków:
print(r_api.content)
print("----")

# z polskimi znakami:
print(r_api.text)
print("----")

# Wyświetlenie poprzez json
read = r_api.json()
print(type(read))
print("----")

print(read)
print("----")

print(type(read[0]))
print("----")

print(read[0])
read_dict = read[0]
print("----")

print(f"Table no {read_dict['no']} from {read_dict['effectiveDate']}.")
print("----")

rates = read_dict['rates']

for rate in rates:
    if rate['mid'] > 3.6:
        print(rate)
        print(type(rate))
        print("----")

# Wyświetlenie w formacie json:
for rate in rates:
    if rate['mid'] > 3.6:
        print(json.dumps(rate, indent=4))

print("----")
