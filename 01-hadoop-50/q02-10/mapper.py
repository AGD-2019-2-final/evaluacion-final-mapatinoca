import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
#! /usr/bin/env python

##
## Esta es la funcion que mapea la entrada a parejas (clave, valor)
##
import sys
if __name__ == "__main__":

    ##
    ## itera sobre cada linea de codigo recibida
    ## a traves del flujo de entrada
    ##
    for line in sys.stdin:
        prop = ""
        valor = 0
                
        line = line.strip()
        splits = line.split(',')
        prop = splits[3]
        valor = splits[4]
        
        print (prop + '\t' + valor)