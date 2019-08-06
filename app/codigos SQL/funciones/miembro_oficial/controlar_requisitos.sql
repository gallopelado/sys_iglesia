CREATE OR REPLACE FUNCTION membresia.controlar_requisitos(idpersona integer, idrequisito integer)
RETURNS boolean as
$$
/**
 * Verifica en la tabla requisitos_cumplidos si existen 
 * registros con esos parámetros.
 * @author: Juan José González Ramírez
 * @email: juanftp100@gmail.com 
 */
BEGIN
	
	PERFORM 
		per_id, req_id, fecha, observacion, creado_por_usuario 
	FROM 
		membresia.requisitos_cumplidos
	WHERE
		per_id = idpersona AND req_id = idrequisito;
	
	IF FOUND THEN
		RETURN TRUE;
	ELSE		
		RETURN FALSE;
	END IF;

END;
$$ LANGUAGE plpgsql;

--SELECT membresia.controlar_requisitos(8, 4);
