import pandas as pd
import re
import numpy as np
import function as F

sant = pd.read_csv("../input/santander.csv") 
bank = pd.read_csv("../input/bankinter.csv")
sab = pd.read_csv("../input/banco-sabadell.csv")
bbva = pd.read_csv("../input/bbva.csv")
caixa = pd.read_csv("../input/caixabank.csv")
banks = [sant, bank, sab, bbva, caixa]