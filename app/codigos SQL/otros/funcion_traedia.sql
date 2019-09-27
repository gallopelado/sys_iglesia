CREATE OR REPLACE FUNCTION trae_dia(date)
RETURNS varchar AS
$$
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
