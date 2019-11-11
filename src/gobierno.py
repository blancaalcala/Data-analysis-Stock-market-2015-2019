import unicodedata
import function as F


def elecciones():
    url = "https://es.wikipedia.org/wiki/Elecciones_generales_de_Espa%C3%B1a_de_"
    urls = ["2011","2016","abril_de_2019"]
    selector = "#mw-content-text > div > table.infobox_v2.vevent > tbody > tr:nth-child" 
    for i in urls:
        data = F.request(url+i)
        if i==urls[0]:
            im = data.findAll('img')[20]
            url_2011 = "https://"+im.get("src")[2:]
            partido_2011 = data.select(selector+"(20) > td:nth-child(2) > b > a")
            votos_2011 = data.select(selector+"(22) > td:nth-child(2)")
            perc_2011 = data.select(selector+"(24) > td:nth-child(2)")
        elif i==urls[1]:
            im = data.findAll('img')[18]
            url_2016 = "https://"+im.get("src")[2:]
            partido_2016 = data.select("#mw-content-text > div > table > tbody > tr:nth-child(21) > td:nth-child(2) > b > a")
            votos_2016 = data.select("#mw-content-text > div > table > tbody > tr:nth-child(23) > td:nth-child(2)")
            perc_2016 = data.select("#mw-content-text > div > table > tbody > tr:nth-child(25) > td:nth-child(2)")
        elif i==urls[2]:
            im = data.findAll('img')[23]
            url_2019 = "https://"+im.get("src")[2:]
            partido_2019 = data.select(selector+"(20) > td:nth-child(2) > b > a")
            votos_2019 = data.select(selector+"(22) > td:nth-child(2)")
            perc_2019 = data.select(selector+"(24) > td:nth-child(2)")

    g_2011 = F.elecciones(partido_2011,votos_2011,perc_2011)
    g_2016 = F.elecciones(partido_2016,votos_2016,perc_2016)
    g_2019 = F.elecciones(partido_2019,votos_2019,perc_2019)
    
    return [g_2011,g_2016,g_2019,[url_2011,url_2016,url_2019]]

