'''
Program will download Gold prices from NBP using API.
'''

import urllib.request
import json


def goldprice_last_days(days):
    prices = []
    try:
        with urllib.request.urlopen(f'http://api.nbp.pl/api/cenyzlota/last/{days}/?format=json') as data:
            data = data.read()
            data = json.loads(data)
            for day in data:
                prices.append({day['data']: day['cena']})
        return prices
    except Exception as e:
        print(f'An error occurs: {e}')

def goldprice_today():
    with urllib.request.urlopen('http://api.nbp.pl/api/cenyzlota/today/?format=json') as today:
        today = today.read()
        today = json.loads(today)
        output = f'{today[0]["data"]} - {today[0]["cena"]} zł'
    return output
