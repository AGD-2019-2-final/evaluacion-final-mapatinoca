import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
##%%writefile reducer.py
##! /usr/bin/python3

##import sys

##
## Esta funcion reduce los elementos que
## tienen la misma clave
##

if __name__ == '__main__':

    curkey = None
    curkey2 = None
    total = 0
    total2 = 0

    
    for line in sys.stdin:
        
        key, val = line.split()
        ##val = float(val)

        if key == curkey:
            
            total += val
        else:
            if curkey is not None:
               
                sys.stdout.write("{}\t{}\t{}\n".format(curkey,total,total2))

            curkey2 = key
            total2 = val
        curkey = key
        total = val

    sys.stdout.write("{}\t{}\t{}\n".format(curkey,total,total2))

