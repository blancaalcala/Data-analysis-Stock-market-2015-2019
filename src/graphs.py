#!/usr/local/bin/python3
import function as F
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


def bank_graphs(df,bol):
    x = 0
    r = [[0]*5]*5    
    bwidth = 0.15
    a1 = np.arange(5)
    fig, ax = plt.subplots()
    colors = ["red","orange","deepskyblue","navy","black"]
    names = ["Santander","Bankinter","Sabadell","BBVA","Caixa"]
    for i in range(0,25,5):
        r[x] = [df['Close'][i],df['Close'][i+1],df['Close'][i+2],df['Close'][i+3],df['Close'][i+4]]
        bars = plt.bar(a1+bwidth*x,r[x],width=bwidth,color=colors[x],zorder=2,label=names[x])
        x+=1
    plt.title("Stock Market"),plt.xlabel("Year"),plt.ylabel("Closed Stock")
    plt.legend(),plt.grid(axis="y")
    save_graph("banks_bar",bol,a1+bwidth,1)
    plt.clf()
    x = 0
    for i in range(0,25,5):
        r[x] = [df['Close'][i],df['Close'][i+1],df['Close'][i+2],df['Close'][i+3],df['Close'][i+4]]
        rects = plt.plot(r[x],color=colors[x],zorder=2,label=names[x])
        x+=1
    plt.title("Stock Market"),plt.xlabel("Year"),plt.ylabel("Closed Stock")
    plt.legend()
    F.save_graph("banks_line",bol,a1+bwidth)


def ind_bank(bank,name,color_b,bol):
    plt.clf()
    values = list(bank["Close"])
    a1 = np.arange(len(values))
    plt.plot(values,color=color_b)
    plt.ylim(0,10)
    plt.title(name+" Stock")
    plt.ylabel('Closed Stock')
    plt.xlabel('Year')
    plt.grid(axis="y")
    plt.grid(axis="x")
    F.save_graph(name,bol,a1)

