#!/usr/local/bin/python3
import requests
import unicodedata
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt


def date_digits(df):
    '''devuelve los 4 digitos de la fecha que corresponden al año'''
    return int(df[:4])

def cut_year(df):
    '''devuelve T/F dependiendo en que filas 
    se cumpla la condicion'''
    return df>2014

def request(url):
    '''web scraping usando BeautifulSoup'''
    res = requests.get(url)
    html = res.text
    return BeautifulSoup(html, 'html.parser')

def csv_read(file):
    '''leer archivo csv from de la carpeta input'''
    return pd.read_csv("../input/"+file+".csv")

def rename_df(df,old,new):
    '''cambiar nombre de una columna en un dataframe de pandas'''
    for i in range(len(old)):
        df = df.rename(columns={old[i]:new[i]})
    return df

def elecciones(partido,voto,perc):
    '''devuelve una lista con informacion a cerca del partido, 
    los votos y el procentaje en unas elecciones'''
    gobierno = []
    gobierno.append(partido[0].text)
    gobierno.append(unicodedata.normalize("NFKD", voto[0].text)[0:10])
    gobierno.append(unicodedata.normalize("NFKD", perc[0].text)[0:7])
    return gobierno

def save_graph(name,bol,sep):
    '''guarda una figura dependiendo de la consulta de los resultados electorales'''
    if not bol:
        plt.xticks(sep,["2015","2016","2017","2018","2019"])
        plt.savefig('../output/'+name+'.png')
    else:
        plt.xticks(sep,["2015 [PP]","2016 [PP]","2017 [PP]","2018 [PP]","2019 [PSOE]"])
        plt.savefig('../output/'+name+'_elecciones.png')

