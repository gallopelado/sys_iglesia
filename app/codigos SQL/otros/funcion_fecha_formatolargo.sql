CREATE OR REPLACE FUNCTION fecha_formatolargo(date)
RETURNS varchar AS
$$
/**
* Funcion fecha_formatolargo
* Permite mediante un tipo date o usando current_date
* convertir la fecha corta DD/MM/YYYY a
* DD MM DEL YYYY
* Autor: Juan José González Ramírez <juanftp100@gmail.com>
* versión: 1.0
*/
BEGIN

	RETURN trae_dia($1) ||' '|| to_char($1, 'dd') ||' '|| trae_mes($1)||' DEL '|| to_char($1, 'YYYY');

END
$$ LANGUAGE plpgsql;


SELECT fecha_formatolargo(current_date);