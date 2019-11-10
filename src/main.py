#!/usr/bin/env python

import argparse
import sys
import subprocess

def recibe_parametros():
    parser = argparse.ArgumentParser(description="Informacion valor stock bancos españoles")
    parser.add_argument('--santander',help='Stock de santander',action='store_true')           
    parser.add_argument('--bankinter',help='Stock de bankinter',action='store_true')
    parser.add_argument('--sabadell',help='Stock de santander',action='store_true')
    parser.add_argument('--bbva',help='Stock de santander',action='store_true')
    parser.add_argument('--caixa',help='Stock de caixa',action='store_true')
    parser.add_argument('--directo',help='Valor Stock en directo',action='store_true')
    parser.add_argument('--elecciones',help='comparar resultados electorales',action='store_true')
    args = parser.parse_args()
    return args

def main():
    print(sys.argv)
    config = recibe_parametros()
    print(config)




if __name__=="__main__":
    main()