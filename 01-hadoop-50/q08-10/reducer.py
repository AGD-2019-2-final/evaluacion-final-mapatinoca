import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
##%%writefile reducer.py
##!/usr/bin/python
##Reducer.py
##import sys

word = {}

##Partitoner
for line in sys.stdin:
    line = line.strip()
    key, val = line.split('\t')

    if key in word:
        word[key].append(float(val))
        
    else:
        word[key] = []
        word[key].append(float(val))
    
##Reducer
for key in word.keys():
    suma = sum(word[key])
    ave_age = sum(word[key])*1.0 / len(word[key])
    
    word[key].sort()
    
    sys.stdout.write("{}\t{}\t{}\n".format(key,suma,ave_age))
