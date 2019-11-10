#!/usr/bin/env python

import pandas as pd
import re
import numpy as np
import function as F
import matplotlib as plt
import sys

pd.options.mode.chained_assignment = None


sant = pd.read_csv("../input/santander.csv") 
bank = pd.read_csv("../input/bankinter.csv")
sab = pd.read_csv("../input/banco-sabadell.csv")
bbva = pd.read_csv("../input/bbva.csv")
caixa = pd.read_csv("../input/caixabank.csv")
banks = [sant, bank, sab, bbva, caixa]
names = ["Santander","Bankinter","Banco Sabadell","BBVA","Caixa Bank"]
for x in range(len(banks)):
    banks[x]["Date"] = banks[x]["Date"].apply(F.date_digits)
    banks[x] = banks[x].loc[(banks[x]["Date"].apply(F.cut_year))]
    banks[x]["Bank"] = names[x]
    banks[x] = banks[x].groupby(["Bank","Date"])["Close", "High", "Low", "Open", "Volume"].mean()

df = pd.concat([banks[0],banks[1],banks[2],banks[3],banks[4]])
print(df)

#GRAFICA





