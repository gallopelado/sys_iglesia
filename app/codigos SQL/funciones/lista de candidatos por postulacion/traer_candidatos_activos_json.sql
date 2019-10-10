CREATE OR REPLACE FUNCTION membresia.traer_candidatos_activos_json()
RETURNS json as
$$
/**
 * Funcion traer_candidatos_activos_json.
 * 
 * Obtiene los candidatos activos en un array de objetos json.
 * 
 */

	SELECT
		array_to_json(
			array_agg(
				data			
			)
		)
	FROM (
	SELECT 
		mp.mper_id AS idmiembro
		, p.per_nombres||' '||p.per_apellidos AS persona
	FROM 
		membresia.miembro_perfil AS mp
	LEFT JOIN referenciales.personas AS p ON mp.mper_id = p.per_id
	WHERE
		mp.mper_estado IS TRUE
	) data;
	
$$ LANGUAGE SQL;

--SELECT membresia.traer_candidatos_activos_json();