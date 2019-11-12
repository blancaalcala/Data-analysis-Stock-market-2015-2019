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
import send as S

def recibe_parametros():
    # obtener parametros true/false para cada tipo de argumento
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
    pdf.cell(200, 10, txt=str(datetime.datetime.now()), ln=1, align="R")
    config = recibe_parametros()

    def write_pdf(text,aligned):
        pdf.cell(200,10,txt=text,ln=1,align=aligned)

    def im_pdf(path,X=80,W=80):
        pdf.image(path,x=X,w=W)
        
    if config.elecciones:
        gob = Gov.elecciones()
        years = ["1","6","9"]
        for i in range(3):
            write_pdf("In 201{} {} obtained {} votes ({}%)".format(years[i],gob[i][0],gob[i][1],gob[i][2]),"L")
            im_pdf(gob[3][i],80,80)
    
    if config.economia:
        if config.elecciones:
            pdf.add_page()
        df = E.pib_ipc()  
        df.plot()
        plt.savefig('../output/economia.png')
        im_pdf("../output/economia.png")
    
    if config.santander and config.bankinter and config.sabadell and config.bbva and config.caixa:
        output = B.bank_data()
        df = pd.concat([output[0],output[1],output[2],output[3],output[4]])
        G.bank_graphs(df,config.elecciones)
        im_pdf("../output/banks_bar.png")
        im_pdf("../output/banks_line.png")

    else:
        output = B.bank_data()
        if config.santander:
            G.ind_bank(output[0],"Santander","red",config.elecciones)
            im_pdf("../output/Santander.png")
        if config.bankinter:
            G.ind_bank(output[1],"Bankinter","orange",config.elecciones)
            im_pdf("../output/Bankinter.png")
        if config.sabadell:
            G.ind_bank(output[2],"Sabadell","deepskyblue",config.elecciones)
            im_pdf("../output/Sabadell.png")
        if config.bbva:
            G.ind_bank(output[3],"BBVA","navy",config.elecciones)
            im_pdf("../output/BBVA.png")
        if config.caixa:
            G.ind_bank(output[4],"CaixaBank","black",config.elecciones)
            im_pdf("../output/CaixaBank.png")

    pdf.add_page()

    if config.stock:
        live = B.stock_directo()
        for x in range(5):
            write_pdf("--> {}: Actual stock closed value: {} Euros".format(live[0][x],live[1][x]),"L")
            write_pdf("--> {}: Previous stock closed value: {} Euros".format(live[0][x],live[2][x]),"L")
        write_pdf("{}".format(live[3]),"L")    

    pdf.output("../output/Pipeline_Proyect.pdf")

    S.send_mail()
    
if __name__=="__main__":
    main()
