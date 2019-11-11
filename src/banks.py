#!/usr/local/bin/python3
 
import sys
import pandas as pd
import function as F
import matplotlib as plt
import requests
from bs4 import BeautifulSoup


pd.set_option('mode.chained_assignment', None)

def bank_data():
    banks = []
    banks.append(F.csv_read("santander"))
    banks.append(F.csv_read("bankinter"))
    banks.append(F.csv_read("banco-sabadell"))
    banks.append(F.csv_read("bbva"))
    banks.append(F.csv_read("caixabank"))
    names = ["Santander","Bankinter","Banco Sabadell","BBVA","Caixa Bank"]
    for x in range(len(banks)):
        banks[x]["Date"] = banks[x]["Date"].apply(F.date_digits)
        banks[x] = banks[x].loc[(banks[x]["Date"].apply(F.cut_year))]
        banks[x]["Bank"] = names[x]
        banks[x] = banks[x].groupby(["Bank","Date"])["Close", "High", "Low", "Open", "Volume"].mean()
    return [banks[0],banks[1],banks[2],banks[3],banks[4]]


def stock_directo():
    links=["https://www.marketwatch.com/investing/stock/san?countrycode=es",
      "https://www.marketwatch.com/investing/stock/bkt?countrycode=es",
      "https://www.marketwatch.com/investing/stock/sab?countrycode=es",
      "https://www.marketwatch.com/investing/stock/bbva?countrycode=es",
      "https://www.marketwatch.com/investing/stock/cabk?countrycode=es"]
    names = ["Banco Santander","Banco Bankinter", "Banco Sabadell", "BBVA", "CaixaBank"]
    actual = []
    previous = []
    for i in range(len(links)):
        res = requests.get(links[i])
        html = res.text
        soup = BeautifulSoup(html, 'html.parser')
        actual.append(soup("span", class_="value")[0].text)
        prev = (soup("span", class_="value")[0].text).encode('cp1252')
        previous.append(prev)
        time = soup("span",class_="timestamp__time")[0].text
    return [names, actual, previous, time]

        





