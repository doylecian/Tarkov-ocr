import json
import urllib.request
import os
import requests
import re


class gameItem:
    def __init__(self, uid, name, short_name, trader_price, avg24, trader_currency, trader_name, template_img):
        self.uid = uid
        self.name = name
        self.short_name = re.sub(r'[\\/*?:"<>|]',"",short_name)
        self.trader_price = trader_price
        self.avg24 = avg24
        self.trader_currency = trader_currency
        self.template_img = template_img
        if self.trader_currency == "$":
            self.trader_price *= 122
        elif self.trader_currency == "€":
            self.trader_price *= 133
        if self.trader_price > 0 and self.avg24 > 0:
            self.profitRatio = (self.trader_price - avg24)
        else:
            self.profitRatio = 0
        self.trader_name = trader_name


gameItems = []
sortedgameItems = []

# LOADING ALL ITEMS INTO LIST
with open('C:\\Users\\Cian\\Desktop\\list.json', encoding='utf-8') as json_file:
    data = json.load(json_file)
    for p in data:
        gameItems.append(gameItem(p['uid'], p['name'], p['shortName'],  p['traderPrice'],  p['avg24hPrice'],
                                  p['traderPriceCur'], p['traderName'], p['img']))


# SORTING ITEMS BY MOST PROFITABLE
sortedGameItems = sorted(gameItems, key=lambda gameitem: gameitem.profitRatio)


def print_all():
    for item in sortedGameItems:
        print(item.name + " | Trader price: " + str(item.trader_price) + "₽ (" + item.trader_name + ") | Flea Price:  " + str(item.avg24) + " | Ratio: " + str(item.profitRatio))


headers = {'User-Agent': 'Mozilla/5.0'}


def download_all():
    for item in sortedGameItems:
        if item.template_img != "" and not os.path.exists('C:\\Users\\Cian\\Desktop\\template_images\\' + item.short_name + ".png"):
            print("Downloading " + item.template_img + " as " + item.short_name)
            url = item.template_img
            print(url)
            response = requests.get(url, headers)

            if response.status_code == 200:
                with open("C:\\Users\\Cian\\Desktop\\template_images\\" + item.short_name + ".png", 'wb') as f:
                    f.write(response.content)


download_all()
