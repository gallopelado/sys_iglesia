CREATE OR REPLACE FUNCTION membresia.verifica_estado_postulacion(idpostulacion integer)
RETURNS boolean AS
$$
/**
* Procedimiento: verifica_estado_postulacion
* Parametros: idpostulacion integer
* Descripcion: Verifica si el registro tiene estado FALSE y no posea fecha procesado.
* Autor: Juan Jose Gonzalez Ramirez <juanftp100@gmail.com>
* Version: 1.0
* Fecha: 07-09-2019
*/
BEGIN

	PERFORM post_id FROM membresia.cabe_postulacion 
	WHERE post_id = idpostulacion AND post_fechaprocesado IS NULL AND post_estado IS TRUE;
	
	IF FOUND THEN
	
		RAISE NOTICE 'Esta postulacion esta habilitada';
		RETURN TRUE;
	
	END IF;

	RAISE EXCEPTION 'Esta postulacion esta desactivada o expirada o no existe';
	RETURN FALSE;

END
$$ LANGUAGE plpgsql;