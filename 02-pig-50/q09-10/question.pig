-- Pregunta
-- ===========================================================================
-- 
-- Para el archivo `data.csv` escriba una consulta en Pig que genere la 
-- siguiente salida:
-- 
--   Vivian@Hamilton
--   Karen@Holcomb
--   Cody@Garrett
--   Roth@Fry
--   Zoe@Conway
--   Gretchen@Kinney
--   Driscoll@Klein
--   Karyn@Diaz
--   Merritt@Guy
--   Kylan@Sexton
--   Jordan@Estes
--   Hope@Coffey
--   Vivian@Crane
--   Clio@Noel
--   Hope@Silva
--   Ayanna@Jarvis
--   Chanda@Boyer
--   Chadwick@Knight
-- 
-- Escriba el resultado a la carpeta `output` del directorio actual.
-- 
fs -rm -f -r output;
--
fs -rm -f -r data.csv
fs -put data.csv

u = LOAD 'data.csv' USING PigStorage(',')
    AS (col1:INT,
		col2:CHARARRAY,
		col3:CHARARRAY,
		col4:CHARARRAY,
		col5:CHARARRAY,
		COL6:INT);


R1 = FOREACH u GENERATE CONCAT($1,'@',$2);
DUMP R1;


STORE R1 INTO 'output';

fs -copyToLocal output output
