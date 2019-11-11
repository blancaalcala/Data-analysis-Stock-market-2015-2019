import function as F
import pandas as pd

def pib_ipc():
    pib = F.csv_read("pib") 
    pib = pib.drop(pib.index[:76])
    pib = pib.drop(pib.index[19:])
    pib = pib.reset_index()

    pib = F.rename_df(pib,["index",'Año;"Periodo";"Variación interanual (en %)"'],["year","PIB %"])
    var = []
    for i in range(len(pib["year"])):
        if pib["year"][i][-1]!='"':
            var.append(int(pib["year"][i][-1]))
            pib["PIB %"][i] = int(pib["PIB %"][i][:-1])/100+var[i]
        else:
            var.append(2)
            pib["PIB %"][i] = 0.00+var[i]
        pib["year"][i] = int(pib["year"][i][0:4])
    pib = pib.groupby("year").sum()/4


    ipc = F.csv_read("ipc") 
    ipc = ipc.drop(ipc.index[50:])
    ipc = ipc.reset_index()

    ipc = F.rename_df(ipc,["index",'Año;"Periodo";"IPC"'],["year","IPC %"])
    var = []
    var = []
    for i in range(len(ipc["year"])):
        var.append(int(ipc["year"][i][-1]))
        ipc["year"][i] = int(ipc["year"][i][0:4])
        ipc["IPC %"][i] = int(ipc["IPC %"][i][:-1])/100+var[i]
        if ipc["year"][i]==2015:
            ipc["IPC %"][i] = ipc["IPC %"][i]/2
        else:
            ipc["IPC %"][i] = ipc["IPC %"][i]/12
    ipc = ipc.groupby("year").sum()
    result = pd.concat([pib,ipc],axis=1)
    return result