CREATE OR REPLACE FUNCTION membresia.persona_requisitos_eliminar(idpersona integer, idrequisito integer)
RETURNS boolean AS
$$
BEGIN
DELETE FROM 
	membresia.requisitos_cumplidos 
WHERE
	per_id = idpersona AND req_id = idrequisito;

RETURN TRUE;
END;
$$ LANGUAGE plpgsql;