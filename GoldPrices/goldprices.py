'''
Program will download Gold prices from NBP using API. It will also show prices in graphical format.
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
                    prices.append({day['data']: round(day['cena'] * 31.1, 2)})
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

    def draw_graph(self, function, *args):
        data = function(*args)
        only_dates = []
        x_ticks = []
        only_prices = []
        months = set()
        for element in data:
            for dates in element.keys():
                only_dates.append(dates)
            for prices in element.values():
                only_prices.append(prices)
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
        # setting max price
        max_price = max(only_prices)
        max_price_date_pos = only_prices.index(max_price)
        max_price_date = only_dates[max_price_date_pos]
        # setting min price
        min_price = min(only_prices)
        min_price_date_pos = only_prices.index(min_price)
        min_price_date = only_dates[min_price_date_pos]
        # creating a graph
        plt.figure()
        plt.plot(only_dates, only_prices)
        plt.grid(True)
        if len(only_dates) > 30:  # setting number of ticks
            plt.xticks(x_ticks, rotation=90, fontsize=8)
        else:
            plt.xticks(only_dates, rotation=90, fontsize=8)
        plt.ylabel("zł/1oz")
        plt.title(f'Gold prices from {only_dates[0]} to {only_dates[-1]}', fontsize=12)
        plt.annotate(f'{max_price:.2f} zł', xy=(max_price_date, max_price),
                     xytext=(max_price_date, max_price))
        plt.annotate(f'{min_price:.2f} zł', xy=(min_price_date, min_price),
                     xytext=(min_price_date, min_price))
        # plt.savefig('wykres.png')
        plt.show()