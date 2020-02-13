-- Pregunta
-- ===========================================================================
-- 
-- Obtenga los cinco (5) valores más pequeños de la 3ra columna.
-- Escriba el resultado a la carpeta `output` del directorio actual.
-- 
fs -rm -f -r output;
--
-- >>> Escriba su respuesta a partir de este punto <<<
--
fs -rm -f -r data.tsv
fs -put data.tsv

u = LOAD './data.tsv' USING PigStorage('\t') AS (f1:CHARARRAY, f2:CHARARRAY, f3:INT);
DUMP u;

R1 = ORDER u BY $2;
R2 = LIMIT R1 5;
R3 = FOREACH R2 GENERATE $2;
DUMP R3;


STORE R3 INTO 'output';

fs -copyToLocal output output