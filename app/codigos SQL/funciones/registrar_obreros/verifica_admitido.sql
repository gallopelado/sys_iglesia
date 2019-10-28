CREATE OR REPLACE FUNCTION membresia.verifica_admitido(idpersona integer, idpostulacion integer)
RETURNS boolean AS
$$
/**
 * Función verifica_admitido
 * Verifica existencia de los registros admitidos de la 
 * postulación.
 * Autor: Juan José González Ramírez <juanftp100@gmail.com>
 */
BEGIN
	PERFORM mo_id, post_id
	FROM membresia.candi_admitidos 
	WHERE mo_id = idpersona AND post_id = idpostulacion;
	IF NOT FOUND THEN
		RAISE EXCEPTION 'Esta persona no esta admitida en la postulación o no existe' USING ERRCODE='20098';
		RETURN FALSE;
	END IF;
	RETURN TRUE;
END;
$$ LANGUAGE plpgsql;

SELECT membresia.verifica_admitido(8,4);