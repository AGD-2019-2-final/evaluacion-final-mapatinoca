import sys
#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
##%%writefile reducer.py
##!/usr/bin/env python
##import sys
#
# >>> Escriba el codigo del reducer a partir de este punto <<<
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

        mes, cont = line.split('\t')
        cont = int(cont)
                
        if mes == curkey:
            
            total += cont
        else:
            
            if curkey is not None:
                
                sys.stdout.write("{}\t{}\n".format(curkey,total))
                
            curkey = mes
            total = cont
                           
    sys.stdout.write("{}\t{}\n".format(curkey,total))
