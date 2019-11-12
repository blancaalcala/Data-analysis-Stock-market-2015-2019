#!/usr/local/bin/python3
import pandas as pd
import function as F
import matplotlib as plt
import requests
from bs4 import BeautifulSoup

pd.set_option('mode.chained_assignment', None)

def bank_data():
    '''limpia y organiza informacion del stock market de los bancos desde 2015'''
    names = ["Santander","Bankinter","Banco Sabadell","BBVA","Caixa Bank"]
    banks = []
    for n in names:
        banks.append(F.csv_read(n))
    for x in range(len(banks)):
        banks[x]["Date"] = banks[x]["Date"].apply(F.date_digits)
        banks[x] = banks[x].loc[(banks[x]["Date"].apply(F.cut_year))]
        banks[x]["Bank"] = names[x]
        banks[x] = banks[x].groupby(["Bank","Date"])["Close", "High", "Low", "Open", "Volume"].mean()
    return [banks[0],banks[1],banks[2],banks[3],banks[4]]

def stock_directo():
    '''consulta en directo el valor de stock de cada banco'''
    sub_links = ["san","bkt","sab","bbva","cabk"]
    names = ["Banco Santander","Banco Bankinter", "Banco Sabadell", "BBVA", "CaixaBank"]
    actual = []
    previous = []
    for i in range(len(sub_links)):
        link= "https://www.marketwatch.com/investing/stock/"+sub_links[i]+"?countrycode=es" 
        soup = F.request(link)
        actual.append(soup.select("body > div.container.wrapper.clearfix.j-quoteContainer.stock > div.region.region--fixed > div.template.template--aside > div > div > div.intraday__data > h3 > bg-quote")[0].text)
        previous.append(soup.select("body > div.container.wrapper.clearfix.j-quoteContainer.stock > div.region.region--fixed > div.template.template--aside > div > div > div.intraday__close > table > tbody > tr > td")[0].text[1:])
        time = soup("span",class_="timestamp__time")[0].text
    return [names, actual, previous, time]







