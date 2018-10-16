'''
Program will download Gold prices from NBP using API.
'''

import urllib.request
import json
import matplotlib.pyplot as plt
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
            output = f'{today[0]["data"]} - {(today[0]["cena"]*31.1):.2f} zł / 1oz'
        return output

    def goldprice_date(self, date):
        try:
            with urllib.request.urlopen(f'http://api.nbp.pl/api/cenyzlota/{date}?format=json') as date:
                date = date.read()
                date = json.loads(date)
                output = f'{date[0]["data"]} - {(date[0]["cena"]*31.1):.2f} zł / 1oz'
            return output
        except Exception as e:
            print(f'An error occurs: {e}')

    def goldprice_daterange(self, start_date, end_date=datetime.date(datetime.today())):
        price_range = []
        try:
            with urllib.request.urlopen(
                    (f'http://api.nbp.pl/api/cenyzlota/{start_date}/{end_date}/?format=json')) as data:
                data = data.read()
                data = json.loads(data)
                for element in data:
                    price_range.append({element['data']: round(element['cena'] * 31.1, 2)})
            return price_range
        except Exception as e:
            print(f'An error occurs: {e}')

    def draw_graph_last_days(self, days):
        last = self.goldprice_last_days(days)
        only_dates = []
        x_ticks = []
        only_prices = []
        months = set()
        for element in last:
            for dates in element.keys():
                only_dates.append(dates)
            for prices in element.values():
                only_prices.append(prices * 31.1)
            for month in element.keys():
                months.add(month[:7])
        for date in only_dates:
            if date[:7] in months:
                x_ticks.append(date)
                months.remove(date[:7])  # a way to avoid duplicates
        if only_dates[0] not in x_ticks:
            x_ticks.insert(0, only_dates[0])  # adding first date to x axis
        if only_dates[-1] not in x_ticks:
            x_ticks.append(only_dates[-1])  # adding last date to x axis
        # creating a graph
        plt.figure()
        plt.plot(only_dates, only_prices)
        plt.grid(True)
        if days > 30:  # setting number of ticks
            plt.xticks(x_ticks, rotation=90)
        else:
            plt.xticks(only_dates, rotation=90)
        plt.ylabel("zł/1oz")
        plt.title(f'Gold prices in last {days} days')
        plt.show()


GoldPrices().draw_graph_last_days(235)
