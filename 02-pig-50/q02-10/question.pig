-- Pregunta
-- ===========================================================================
-- 
-- Ordene el archivo `data.tsv`  por letra y valor (3ra columna).
-- Escriba el resultado a la carpeta `output` del directorio actual.
-- 
fs -rm -f -r output;
-- 
--  >>> Escriba el codigo del mapper a partir de este punto <<<
-- 
fs -rm -f -r data.tsv
fs -put data.tsv

u = LOAD './data.tsv' USING PigStorage('\t') AS (f1:CHARARRAY, f2:CHARARRAY, f3:INT);
DUMP u;

y= ORDER u BY $0, $2;
DUMP y;

STORE y INTO 'output';

fs -copyToLocal output output
