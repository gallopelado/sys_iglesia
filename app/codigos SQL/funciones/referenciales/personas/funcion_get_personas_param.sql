
/*CREATE TYPE referenciales.td_persona_tipo AS (idpersona integer, cedula varchar, persona varchar, idtipopersona integer, tipo varchar, 
obs varchar, fechabaja date, razonbaja razonbaja);*/
--DROP TYPE referenciales.td_persona_tipo
/**
 * Funcion: referenciales.get_personas(integer)
 * Descripcion: Retorna todos los datos de personas
 * segun id.
 */
CREATE OR REPLACE FUNCTION referenciales.get_personas(integer)
RETURNS SETOF referenciales.td_persona_tipo AS
$$

	SELECT
		p.per_id idpersona,
		p.per_ci cedula,
		p.per_nombres || ' ' || p.per_apellidos persona,
		p.tipoper_id idtipo,
		tip.tipoper_des tipo,
		p.per_obs obs,
		p.per_fechabaja fechabaja,
		p.per_razonbaja 
	FROM
		referenciales.personas p
	INNER JOIN
		referenciales.tipo_persona tip
		ON p.tipoper_id = tip.tipoper_id
	WHERE
		p.per_id = $1;

$$ LANGUAGE SQL;
--DROP FUNCTION referenciales.get_personas_id(idpersona integer)
SELECT * FROM referenciales.get_personas();