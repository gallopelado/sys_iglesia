CREATE OR REPLACE FUNCTION trae_mes(date)
RETURNS varchar AS
$$
/**
* Función trae_mes.
* 
* Según current_date obtiene el numero del día,
* se compara con un string para obtener el 
* nombre del día.
* Ej: 1 es DOMINGO, 7 es SABADO
*
* Autor: Juan José González Ramírez <juanftp100@gmail.com>
* Versión: 1.0
* Fecha: 30-09-2019
*/
DECLARE
	v_mes varchar;
BEGIN

	CASE to_char($1, 'mm')
		WHEN '01' THEN
			v_mes := 'ENERO';
		WHEN '02' THEN
			v_mes := 'FEBRERO';
		WHEN '03' THEN
			v_mes := 'MARZO';
		WHEN '04' THEN
			v_mes := 'ABRIL';
		WHEN '05' THEN
			v_mes := 'MAYO';
		WHEN '06' THEN
			v_mes := 'JUNIO';
		WHEN '07' THEN
			v_mes := 'JULIO';
		WHEN '08' THEN
			v_mes := 'AGOSTO';
		WHEN '09' THEN
			v_mes := 'SEPTIEMBRE';
		WHEN '10' THEN
			v_mes := 'OCTUBRE';
		WHEN '11' THEN
			v_mes := 'NOVIEMBRE';
		WHEN '12' THEN
			v_mes := 'DICIEMBRE';
	END CASE;
	
	RETURN v_mes;

END
$$ LANGUAGE plpgsql;

SELECT trae_mes(current_date);