-- 
-- Pregunta
-- ===========================================================================
-- 
-- Para el archivo `data.tsv` Calcule la cantidad de registros por clave de la 
-- columna 3. En otras palabras, cuántos registros hay que tengan la clave 
-- `aaa`?
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

R1 = FOREACH u GENERATE FLATTEN($2);
R2 = FOREACH R1 GENERATE $0;
R3 = GROUP R2 BY $0;
R4 = FOREACH R3 GENERATE CONCAT($0,',',(CHARARRAY)COUNT($1));
DUMP R4;


STORE R4 INTO 'output';

fs -copyToLocal output output