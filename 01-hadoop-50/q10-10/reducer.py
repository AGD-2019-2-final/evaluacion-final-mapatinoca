##!/usr/bin/env python

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
    vec1 = ""
    vec2 = ""
    vec3 = ""
    vec4 = ""
    vec5 = ""
    vec6 = ""
    vec7 = ""
    vec8 = ""
    
    ##
    ## cada linea de texto recibida es una
    ## entrada clave \tabulador valor
    ##
    for line in sys.stdin:

        letra, orden, valor  = line.split('\t')
        valor = int(valor)
                       
        if letra == 'A':
            vec1 =vec1 + str(valor) + ','
            ultiLetra = letra
            
        if letra == 'B':
            if ultiLetra != letra:
                temp = len(vec1)
                texto = vec1[:temp-1]
                print(ultiLetra+'\t'+texto)
                
            vec2 =vec2 + str(valor) + ','
            ultiLetra = letra
            
        if letra == 'C':
            if ultiLetra != letra:
                temp = len(vec2)
                texto = vec2[:temp-1]
                print(ultiLetra+'\t'+texto)
                
            vec3 =vec3 + str(valor) + ','
            ultiLetra = letra
            
        if letra == 'D':
            if ultiLetra != letra:
                temp = len(vec3)
                texto = vec3[:temp-1]
                print(ultiLetra+'\t'+texto)
                
            vec4 =vec4 + str(valor) + ','
            ultiLetra = letra
            
        if letra == 'F':
            if ultiLetra != letra:
                temp = len(vec4)
                texto = vec4[:temp-1]
                print(ultiLetra+'\t'+texto)
                
            vec5 =vec5 + str(valor) + ','
            ultiLetra = letra
            
        if letra == 'G':
            if ultiLetra != letra:
                temp = len(vec5)
                texto = vec5[:temp-1]
                print(ultiLetra+'\t'+texto)
                
            vec6 =vec6 + str(valor) + ','
            ultiLetra = letra
            
        if letra == 'H':
            if ultiLetra != letra:
                temp = len(vec6)
                texto = vec6[:temp-1]
                print(ultiLetra+'\t'+texto)
                
            vec7 =vec7 + str(valor) + ','
            ultiLetra = letra
            
        if letra == 'I':
            if ultiLetra != letra:
                temp = len(vec7)
                texto = vec7[:temp-1]
                print(ultiLetra+'\t'+texto)
                
            vec8 =vec8 + str(valor) + ','
            ultiLetra = letra
            
            if valor == 27:
                temp = len(vec8)
                texto = vec8[:temp-1]
                print(ultiLetra+'\t'+texto)
