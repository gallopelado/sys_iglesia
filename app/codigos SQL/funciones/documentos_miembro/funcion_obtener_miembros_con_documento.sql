-- Traer todos los miembros que tengan documentos.
CREATE OR REPLACE FUNCTION membresia.cantidaddocumentos_miembro()
RETURNS SETOF membresia.t_documentos_miembro AS
$$
BEGIN

	RETURN QUERY
	SELECT 
	
		d.per_id idpersona,
		per.per_nombres||' '||per.per_apellidos persona,
		count(*) as "Cantidad de documentos registrados"
		
	FROM 
		membresia.documentos_miembro d
	LEFT JOIN referenciales.personas per ON
	d.per_id = per.per_id
	
	group by idpersona, persona order by idpersona ASC;
	IF not found THEN
		RAISE WARNING 'No existen miembros con documentos registrados';
	END IF;
	
	RETURN;
	
END;
$$ LANGUAGE plpgsql;

-- Crear el TYPE
--CREATE TYPE membresia.t_documentos_miembro AS (idpersona integer, persona text, "Cantidad_documentos" bigint);
--DROP TYPE t_documentos_miembro;
--DROP FUNCTION membresia.cantidaddocumentos_miembro();
--SELECT membresia.cantidaddocumentos_miembro();