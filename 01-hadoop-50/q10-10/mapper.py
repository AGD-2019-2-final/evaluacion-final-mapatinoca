##! /usr/bin/env python
###   MAPPER ###
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
        letra = ""
        valor = 0
        valor2 = 0
        v = ""
                
        line = line.strip()
        splits = line.split('\t')
        valor = (splits[0]).strip()
        letras = (splits[1]).strip()
        let = letras.split(',')
        
        ##sys.stdout.write("{}\t{}\t{}\n".format(let,valor,letras))
        
        for i in range(0,len(let)):
            
            print(let[i]+'\t'+str((float(valor))/100)+'\t'+valor)
