CREATE OR REPLACE FUNCTION trae_dia(date)
RETURNS varchar AS
$$
/**
* Función trae_dia.
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
	v_dia varchar;
BEGIN
	
	CASE to_char($1, 'd')
		
		WHEN '1' THEN
		
			v_dia := 'DOMINGO';
		
		WHEN '2' THEN
		
			v_dia := 'LUNES';
		
		WHEN '3' THEN
		
			v_dia := 'MARTES';
		
		WHEN '4' THEN
		
			v_dia := 'MIERCOLES';
		
		WHEN '5' THEN 
		
			v_dia := 'JUEVES';
		
		WHEN '6' THEN
		
			v_dia := 'VIERNES';
		
		WHEN '7' THEN
		
			v_dia := 'SABADO';
		
	END CASE;

	RETURN v_dia;
END
$$ LANGUAGE PLPGSQL;

SELECT public.trae_dia(current_date);
