#!/usr/local/bin/python3
import requests
import unicodedata
from bs4 import BeautifulSoup
import pandas as pd


def date_digits(df):
    return int(df[:4])

def cut_year(df):
    return df>2014

def request(url):
    res = requests.get(url)
    html = res.text
    return BeautifulSoup(html, 'html.parser')

def csv_read(file):
    return pd.read_csv("../input/"+file+".csv")

def rename_df(df,old,new):
    for i in range(len(old)):
        df = df.rename(columns={old[i]:new[i]})
    return df

def elecciones(partido,voto,perc):
    gobierno = []
    gobierno.append(partido[0].text)
    gobierno.append(unicodedata.normalize("NFKD", voto[0].text)[0:10])
    gobierno.append(unicodedata.normalize("NFKD", perc[0].text)[0:7])
    return gobierno

def resultados(gob):
    years = ["2011","2016","2019"]
    for i in range(len(gob)):
        print("\n{} ganó las elecciones de {} con {} votos ({})".format(gob[i][0],years[i],gob[i][1],gob[i][2]))
    return " "

def save_graph(name,bol,sep):
    if not bol:
        plt.xticks(sep,["2015","2016","2017","2018","2019"])
        plt.savefig('../output/'+name+'.png')
    else:
        plt.xticks(sep,["2015 [PP]","2016 [PP]","2017 [PP]","2018 [PP]","2019 [PSOE]"])
        plt.savefig('../output/'+name+'_elecciones.png')

