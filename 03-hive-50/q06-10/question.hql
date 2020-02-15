-- 
-- Pregunta
-- ===========================================================================
--
-- Escriba una consulta que retorne unicamente la columna t0.c5 con sus 
-- elementos en mayuscula.
--
-- Escriba el resultado a la carpeta `output` de directorio de trabajo.
--
DROP TABLE IF EXISTS tbl0;
CREATE TABLE tbl0 (
    c1 INT,
    c2 STRING,
    c3 INT,
    c4 DATE,
    c5 ARRAY<CHAR(1)>, 
    c6 MAP<STRING, INT>
)
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ','
COLLECTION ITEMS TERMINATED BY ':'
MAP KEYS TERMINATED BY '#'
LINES TERMINATED BY '\n';
LOAD DATA LOCAL INPATH 'tbl0.csv' INTO TABLE tbl0;
--
DROP TABLE IF EXISTS tbl1;
CREATE TABLE tbl1 (
    c1 INT,
    c2 INT,
    c3 STRING,
    c4 MAP<STRING, INT>
)
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ','
COLLECTION ITEMS TERMINATED BY ':'
MAP KEYS TERMINATED BY '#'
LINES TERMINATED BY '\n';
LOAD DATA LOCAL INPATH 'tbl1.csv' INTO TABLE tbl1;
--
-- >>> Escriba su respuesta a partir de este punto <<<
--
INSERT OVERWRITE LOCAL DIRECTORY 'output'
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
STORED AS TEXTFILE


--SELECT upper (NVL(c5[0],'')),
--upper (NVL(c5[1],'')),
--upper (NVL(c5[2],'')),
--upper (NVL(c5[3],'')),
--upper (NVL(c5[4],''))
--FROM tbl0;

SELECT CONCAT(UPPER(c5[0]),':', UPPER(c5[1]), CASE WHEN c5[2] IS NULL THEN '' ELSE CONCAT(':',UPPER(c5[2])) END, CASE WHEN c5[3] IS NULL THEN '' ELSE CONCAT(':',UPPER(c5[3])) END, CASE WHEN c5[4] IS NULL THEN '' ELSE CONCAT(':', UPPER(c5[4])) END) FROM tbl0;


