#!/usr/local/bin/python3
import requests
import unicodedata
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt


def date_digits(df):
    '''cortar digitos de fecha para obtener solo los digitos del año'''
    return int(df[:4])

def cut_year(df):
    '''obtener datos que cumplan la condicion'''
    return df>2014

def request(url):
    '''web scraping con beautiful soup'''
    res = requests.get(url)
    html = res.text
    return BeautifulSoup(html, 'html.parser')

def csv_read(file):
    '''leer fichero csv'''
    return pd.read_csv("../input/"+file+".csv")

def rename_df(df,old,new):
    '''cambiar nomnbre a una columna de pandas df'''
    for i in range(len(old)):
        df = df.rename(columns={old[i]:new[i]})
    return df

def elecciones(partido,voto,perc):
    '''crea una lista con '''
    gobierno = []
    gobierno.append(partido[0].text)
    gobierno.append(unicodedata.normalize("NFKD", voto[0].text)[0:10])
    gobierno.append(unicodedata.normalize("NFKD", perc[0].text)[0:7])
    return gobierno

def save_graph(name,bol,sep):
    '''guarda el eje x de ls graficas dependiendo de la consulta de las elecciones'''
    if not bol:
        plt.xticks(sep,["2015","2016","2017","2018","2019"])
        plt.savefig('../output/'+name+'.png')
    else:
        plt.xticks(sep,["2015 [PP]","2016 [PP]","2017 [PP]","2018 [PP]","2019 [PSOE]"])
        plt.savefig('../output/'+name+'.png')

