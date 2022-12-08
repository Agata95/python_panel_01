import requests
import json


def nbp_read(code, start_date, end_date):
    try:
        api_link = f"http://api.nbp.pl/api/exchangerates/rates/A/{code}/{start_date}/{end_date}/"
        r_api = requests.get(api_link)
        read = r_api.json()
        result = [rate['mid'] for rate in read['rates']]

        print(f"Currency {code} are: {result}")
    except:
        print(f'Your values are incorrect!')


nbp_read("CHF", "2022-11-01", "2022-11-11")
print('----')
nbp_read("CHI", "2022-11-01", "2022-11-11")
print('----')
