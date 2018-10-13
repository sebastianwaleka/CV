'''
Program will download Gold prices from NBP using API.
'''

import urllib.request
import json
from datetime import datetime

class GoldPrices:
    def goldprice_last_days(self, days):
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

    def goldprice_today(self):
        with urllib.request.urlopen('http://api.nbp.pl/api/cenyzlota/today/?format=json') as today:
            today = today.read()
            today = json.loads(today)
            output = f'{today[0]["data"]} - {(today[0]["cena"]*31.1):.2f} zł'
        return output

    def goldprice_date(self, date):
        try:
            with urllib.request.urlopen(f'http://api.nbp.pl/api/cenyzlota/{date}?format=json') as date:
                date = date.read()
                date = json.loads(date)
                output = f'{date[0]["data"]} - {(date[0]["cena"]*31.1):.2f} zł'
            return output
        except Exception as e:
            print(f'An error occurs: {e}')

    def goldprice_daterange(self, start_date, end_date=datetime.date(datetime.today())):
        price_range = []
        try:
            with urllib.request.urlopen((f'http://api.nbp.pl/api/cenyzlota/{start_date}/{end_date}/?format=json')) as data:
                data = data.read()
                data = json.loads(data)
                for element in data:
                    price_range.append({element['data']: round(element['cena']*31.1, 2)})
            return price_range
        except Exception as e:
            print(f'An error occurs: {e}')
