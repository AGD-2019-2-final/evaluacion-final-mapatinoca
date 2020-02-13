-- 
-- Pregunta
-- ===========================================================================
-- 
-- Para responder la pregunta use el archivo `data.csv`.
-- 
-- Escriba el código equivalente a la siguiente consulta SQL.
-- 
--    SELECT 
--        firstname, 
--        LOCATE('ia', firstname) 
--    FROM 
--        u;
-- 
-- Escriba el resultado a la carpeta `output` del directorio actual.
-- 
fs -rm -f -r output;
--
u = LOAD 'data.csv' USING PigStorage(',') 
    AS (id:int, 
        firstname:CHARARRAY, 
        surname:CHARARRAY, 
        birthday:CHARARRAY, 
        color:CHARARRAY, 
        quantity:INT);
--
-- >>> Escriba su respuesta a partir de este punto <<<
--
fs -rm -f -r data.csv;
fs -put data.csv

s = FILTER u BY SUBSTRING ($1, 0, 1) >='A';
t = FOREACH s GENERATE INDEXOF($1, 'ia', 0);

DUMP t;

STORE t INTO 'output';
fs -copyToLocal output output;