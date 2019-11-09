#!/usr/bin/env python3 


import argparse
import sys
import subprocess

def recibeConfig():
	parser = argparse.ArgumentParser(description="Informacion valor stock bancos españoles")                 

	parser.add_argument('--santander', help='Stock de santander', action='store_true')           
	parser.add_argument('--bankinter', help='Stock de bankinter', action='store_true')
	parser.add_argument('--sabadell', help='Stock de santander', action='store_true')
	parser.add_argument('--bbva', help='Stock de santander', action='store_true')
    parser.add_argument('--caixa', help='Stock de santander', action='store_true')
    parser.add_argument('--directo', help='Valor Stock en directo', action='store_true')
    parser.add_argument('--elecciones', help='comparar resultados electorales ', action='store_true')
    args = parser.parse_args()
    print(args)
    return args

def main():

    print(sys.argv)
    
    config = recibeConfig()
    
    print("Hola {}".format(config.santander))

if __name__=="__main__":
    main()