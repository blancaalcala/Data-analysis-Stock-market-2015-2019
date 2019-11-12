# PIPELINE PROYECT

cada uno de los ficheros tienen una funcion dentro del programa:

## BANKS:
### bank_data()
limpia y organiza la informacion del valor en bolsa de distintos bancos españoles
### stock_directo()
consulta con web scraping el valor en directo del valor en bolsa de cada banco

## ECONOMIA
### pib_ipc()
procesa y limpia dos ficheros csv con informacion a cerca del PIB e IPC de España desde 2015

## GOBIERNO
### elecciones()
web scraping para obtener informacion a cerca de los resultados electorales de 2011, 2016 y 2019

## GRAPHS
### bank_graphs()
crea dos tipos de graficas (de barras y de lineas 2D) para visualizar la evolucion del balor en bolsa de todos los bancos desde 2015
### ind_bank()
crea graficas individuales para cada banco seleccionado mostrando la evolucion de su valor en bolsa

## SEND
### send_mail()
recibe las direcciones de email y manda el pdf guardado por email como archivo adjunto

## MAIN
### recibe_parametros()
con arg obtenemos los parametros de entrada al fichero principal en forma de true o false
### main()
crea un pdf al que se le van añadiendo los resultados obtenidos a partir de las siguientes funciones, que luego sera enviado por email al llamar a la funcion send_mail




