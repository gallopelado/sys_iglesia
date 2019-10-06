CREATE OR REPLACE FUNCTION membresia.anular_postulacion(idpostulacion integer)
RETURNS boolean AS
$$
/**
* Procedimiento: anular_postulacion
* Parametros: idpostulacion integer
* Descripcion: Anular postulacion por demanda.
* Autor: Juan José González Ramírez <juanftp100@gmail.com>
* Version: 1.0
* Fecha: 08-09-2019
*/
BEGIN

	PERFORM post_id FROM membresia.cabe_postulacion
	WHERE post_id = idpostulacion;
	IF NOT FOUND THEN
		RAISE NOTICE 'No existe esta postulacion';
		RETURN FALSE;
	END IF;

	UPDATE membresia.cabe_postulacion 
	SET post_estado = FALSE
	WHERE post_id = idpostulacion;
	
	RAISE NOTICE 'Se anulo correctamente la postulacion';
	RETURN TRUE;
	
END
$$ LANGUAGE plpgsql;