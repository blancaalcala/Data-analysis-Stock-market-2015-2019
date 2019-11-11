#!/usr/local/bin/python3
import argparse
import sys
import banks as B
import graphs as G
import economia as E
import gobierno as Gov
import function as F
from fpdf import FPDF
import datetime
from pandas.plotting import table
import matplotlib.pyplot as plt
import pandas as pd

def recibe_parametros():
    '''recibe argumentos en forma de true/false'''
    parser = argparse.ArgumentParser(description="Informacion valor stock bancos españoles")
    parser.add_argument('-san','--santander',help='Ver evolucion de stock de santander',action='store_true')           
    parser.add_argument('-bank','--bankinter',help='Ver evolucion de stock de bankinter',action='store_true')
    parser.add_argument('-sab','--sabadell',help='Ver evolucion de stock de santander',action='store_true')
    parser.add_argument('--bbva',help='Ver evolucion de stock de santander',action='store_true')
    parser.add_argument('--caixa',help='Ver evolucion de stock de caixa',action='store_true')
    parser.add_argument('--stock',help='Ver valor Stock en directo de todos los bancos',action='store_true')
    parser.add_argument('--economia',help='Consultar parametros economia española',action='store_true')
    parser.add_argument('--elecciones',help='Consultar resultados electorales',action='store_true')
    args = parser.parse_args()
    return args

def main():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=11)
    pdf.cell(200, 10, txt=str(datetime.datetime.now().date()), ln=1, align="R")

    def write_pdf(text,aligned):
        '''escribe el string text en el pdf''' 
        pdf.cell(200,10,txt=text,ln=1,align=aligned)
    
    config = recibe_parametros()
    
    if config.santander and config.bankinter and config.sabadell and config.bbva and config.caixa:
        output = B.bank_data()
        df = pd.concat([output[0],output[1],output[2],output[3],output[4]])
        G.bank_graphs(df,config.elecciones)
    else:
        output = B.bank_data()
        if config.santander:
            G.ind_bank(output[0],"Santander","red",config.elecciones)
        if config.bankinter:
            G.ind_bank(output[1],"Bankinter","orange",config.elecciones)
        if config.sabadell:
            G.ind_bank(output[2],"Sabadell","deepskyblue",config.elecciones)
        if config.bbva:
            G.ind_bank(output[3],"BBVA","navy",config.elecciones)
        if config.caixa:
            G.ind_bank(output[4],"CaixaBank","black",config.elecciones)
    if config.stock:
        live = B.stock_directo()
        for x in range(5):
            write_pdf("{}: Actual stock closed value: {} Euros".format(live[0][x],live[1][x]),"L")
            write_pdf("{}: Previous stock closed value: {} Euros".format(live[0][x],live[2][x]),"L")
        write_pdf("{}".format(live[3]),"L")    
    if config.economia:
        df = E.pib_ipc()  
        df.plot()
        plt.savefig('../output/mytable.png')
    if config.elecciones:
        gob = Gov.elecciones()
        years = ["1","6","9"]
        for i in range(3):
            write_pdf("\nIn 201{} {} obtained {} votes ({}%)".format(years[i],gob[i][0],gob[i][1],gob[i][2]),"L")
            pdf.image(gob[3][i],x=60)
   
    pdf.output("../output/Pipeline_Proyect.pdf")


if __name__=="__main__":
    main()
