import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
#!/usr/bin/env python

import sys

##
## Esta funcion reduce los elementos que
## tienen la misma clave
##

if __name__ == '__main__':

    curkey = None
    temp = 0
    ultiLetra = None
    valor = 0
    ultVal = None
    vector = []
    
    ##
    ## cada linea de texto recibida es una
    ## entrada clave \tabulador valor
    ##
    for line in sys.stdin:

        val, valor, fecha, letra  = line.split('\t')
        valor = int(valor)
        letra = letra.strip()
                        
                   
    ##print("resp...", ultiProp, ultVal)
        ##sys.stdout.write("{}\t{}".format(letra,fecha+'1'))
        if valor <= 7:
            print(letra+'\t'+fecha+'\t'+str(valor))