import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
##%%writefile mapper.py
##! /usr/bin/python3

##
## Esta es la funcion que mapea la entrada a parejas (clave, valor)
##
##import sys
if __name__ == "__main__":

    ##
    ## itera sobre cada linea de codigo recibida
    ## a traves del flujo de entrada
    ##        
    for line in sys.stdin:
        letra = ""
        valor = ""
        cantidad = 0
        
        line = line.strip()
        splits = line.split()
        letra = splits[0]
        valor = splits[2]

        ##
        ## genera las tuplas palabra \tabulador 1
        ## ya que es un conteo de palabras
        ##
            ##
            ## escribe al flujo estandar de salida
            ##
        sys.stdout.write("{}\t{}\n".format(letra,valor))