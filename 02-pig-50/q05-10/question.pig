-- 
-- Pregunta
-- ===========================================================================
-- 
-- Para el archivo `data.tsv` compute Calcule la cantidad de registros en que 
-- aparece cada letra minúscula en la columna 2.
-- 
-- Escriba el resultado a la carpeta `output` del directorio actual.
-- 
fs -rm -f -r output;
--
-- >>> Escriba su respuesta a partir de este punto <<<
--
fs -rm -f -r data.tsv
fs -put data.tsv

u = LOAD 'data.tsv' USING PigStorage('\t')
    AS (col1:CHARARRAY,
        col2:BAG{t: TUPLE(p:CHARARRAY)},
        col3:MAP[]);

R1 = FOREACH u GENERATE FLATTEN($1);
R2 = GROUP R1 BY $0;
R3 = FOREACH R2 GENERATE CONCAT($0,'\t',(CHARARRAY)COUNT($1));
DUMP R3;


STORE R3 INTO 'output';

fs -copyToLocal output output