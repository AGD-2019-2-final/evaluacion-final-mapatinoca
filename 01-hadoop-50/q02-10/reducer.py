import sys
#
#  >>> Escriba el codigo del reducer a partir de este punto <<<
#
#!/usr/bin/env python

import sys

##
## Esta funcion reduce los elementos que
## tienen la misma clave
##

if __name__ == '__main__':

    curkey = None
    total = 0
    ultiProp = None
    valor = None
    ultVal = None

    ##
    ## cada linea de texto recibida es una
    ## entrada clave \tabulador valor
    ##
    for line in sys.stdin:

        prop, val = line.split("\t")
        val = int(val)     
        
        if ultiProp is None:
            ultVal = val
            
             
        if ultiProp == prop:
            ultVal = max(ultVal,val)
            
        else:
            
            if not(ultiProp is None):
            
                sys.stdout.write("{}\t{}\n".format(ultiProp,ultVal))
            
            ultiProp = prop
            ultVal = val
            
            
    ##print("resp...", ultiProp, ultVal)
    sys.stdout.write("{}\t{}\n".format(ultiProp,ultVal))