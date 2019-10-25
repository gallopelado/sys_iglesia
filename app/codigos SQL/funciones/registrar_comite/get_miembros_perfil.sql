CREATE OR REPLACE FUNCTION membresia.get_miembros_perfil()
RETURNS json AS $$
/**
 * Funcion get_miembros_perfil
 * Devuelve un array de objetos json
 * de los datos de miembros con perfil.
 * Autor: Juan José González Ramírez <juanftp100@gmail.com>
 */	
SELECT
	array_to_json( array_agg( row_to_json( datos ) ) ) resultado
FROM (
	SELECT
		mp.mper_id idmiembro
		, p.per_nombres || ' ' || p.per_apellidos miembro
	FROM 
		membresia.miembro_perfil AS mp
	LEFT JOIN
		referenciales.personas AS p ON mp.mper_id = p.per_id
	WHERE
		mp.mper_estado IS TRUE
)datos;

$$ LANGUAGE SQL;

SELECT membresia.get_miembros_perfil();