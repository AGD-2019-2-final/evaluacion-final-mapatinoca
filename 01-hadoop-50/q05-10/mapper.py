import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
##%%writefile mapper.py
##! /usr/bin/env python
##import sys
if __name__ == "__main__":

    ##
    ## itera sobre cada linea de codigo recibida
    ## a traves del flujo de entrada
    ##
    for line in sys.stdin:
        letra = ""
        valor = 0
                
        line = line.strip()
        splits = line.split()
        letra = splits[0]
        fecha = splits[1]
        valor = splits[2]
        
        anio, mes, dia = fecha.split('-')
        
        sys.stdout.write("{}\t1\n".format(mes))
