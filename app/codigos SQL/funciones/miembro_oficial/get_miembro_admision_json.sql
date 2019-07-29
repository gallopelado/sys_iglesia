CREATE OR REPLACE FUNCTION membresia.get_miembro_admision_json(bool)
RETURNS json AS
/**
 * Funcion: get_miembro_admision_json.
 * Parametros: estado booleano.
 * Descripción: Obtiene todas las admisiones activas o inactivas.
 */
$$
SELECT 
	array_to_json(array_agg(row_to_json(consulta)))
FROM
	(SELECT idadmision, persona FROM membresia.get_miembro_admision(true)) consulta;
$$ LANGUAGE SQL;

