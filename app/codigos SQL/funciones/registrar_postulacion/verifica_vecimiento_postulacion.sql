CREATE OR REPLACE PROCEDURE membresia.verifica_vecimiento_postulacion()
LANGUAGE plpgsql
AS $$
/**
* Procedimiento:verifica_vecimiento_postulacion
* Parametros:
* Descripcion: Verifica si la fecha de finalización coincide
* con la fecha actual, entoces cambia el estado del registro.
* Autor: Juan José González Ramírez <juanftp100@gmail.com>
* Version: 1.0
* Fecha: 04-10-2019
*/
DECLARE 
	v_detectado boolean := FALSE;
	reg record;
	fecha_actual date := current_date;
BEGIN
	
	FOR reg IN SELECT post_finpostu, post_id FROM membresia.cabe_postulacion WHERE post_estado IS TRUE AND post_fechaprocesado IS NULL
	LOOP
	
		-- Si vence hoy, actualizamos el estado y la fecha de procesado
		IF reg.post_finpostu = fecha_actual THEN
		
			v_detectado := TRUE;
					
			UPDATE membresia.cabe_postulacion SET post_estado = FALSE, post_fechaprocesado = fecha_actual
			WHERE post_id = reg.post_id;
						
		END IF;
		
	END LOOP;

	IF v_detectado = TRUE THEN
		RAISE NOTICE 'Se actualizó uno o más registros';
	ELSE
		RAISE NOTICE 'No se actualizó ningún registro';
	END IF;
	
END
$$;