CREATE OR REPLACE FUNCTION referenciales.get_personas_activas()
RETURNS SETOF referenciales.td_persona_simple AS
$$
	
	SELECT
		per_id idpersona,
		per_nombres ||' '|| per_apellidos persona	
	FROM
			referenciales.personas
	WHERE
			per_fechabaja IS NULL;
			
	

$$ LANGUAGE sql;
--DROP FUNCTION referenciales.get_personas_activas()
SELECT * FROM referenciales.get_personas_activas();