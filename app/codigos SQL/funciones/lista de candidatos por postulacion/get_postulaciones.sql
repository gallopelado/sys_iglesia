CREATE OR REPLACE FUNCTION membresia.get_postulaciones(opcion varchar)
RETURNS TABLE(idpostulacion integer, descripcion text, estado text) AS
$$
/**
* Función get_postulaciones.
* Obtiene postulaciones registradas según estado, los cuales son:
* ABIERTA, CERRADA, ANULADA, ''.
* EL '' significa que obtenga todos los registros sin importar
* su estado.
*
* Autor: Juan José González Ramírez <juanftp100@gmail.com>
*/
	SELECT
		post_id
		, post_des
		, (
			CASE WHEN post_fechaprocesado IS NULL AND post_estado IS TRUE THEN 'ABIERTA' 
				WHEN post_fechaprocesado IS NOT NULL AND post_estado IS FALSE THEN 'CERRADA'
				WHEN post_fechaprocesado IS NULL AND post_estado IS FALSE THEN 'ANULADA' 
			END
		)
	FROM
		membresia.cabe_postulacion	
		WHERE
			CASE opcion
			WHEN 'ABIERTA' THEN
				post_fechaprocesado IS NULL AND post_estado IS TRUE
			WHEN 'CERRADA' THEN
				post_fechaprocesado IS NOT NULL AND post_estado IS FALSE
			WHEN 'ANULADA' THEN
				post_fechaprocesado IS NULL AND post_estado IS FALSE
			WHEN 'TODAS' THEN
				post_id IS NOT NULL
			END;

$$ LANGUAGE sql;

SELECT * FROM membresia.get_postulaciones('');