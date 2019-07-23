/*
 * Funcion get_data_persona_requisito
 * Descripcion: Según id de persona, se debe obtener
 * nombre y apellido del sujeto, requisito ligados al registro
 * con su id, descripción, observacion.(Personas sin fecha de baja y razon.)
 */

CREATE OR REPLACE FUNCTION membresia.get_data_persona_requisito
(INOUT idpersona integer, OUT cedula varchar, OUT persona text, OUT observacion varchar,
OUT idrequisito integer, OUT requisito varchar)
RETURNS SETOF record AS
$$
SELECT 
	p.per_id idpersona, 
	p.per_ci cedula,
	p.per_nombres || ' ' || p.per_apellidos persona,	
	rc.observacion observacion,
	rc.req_id idrequisito,
	req.req_des requisito
FROM 
	referenciales.personas p
LEFT JOIN
	membresia.requisitos_cumplidos rc ON p.per_id = rc.per_id
INNER JOIN
	referenciales.requisitos req ON rc.req_id = req.req_id
WHERE 
	p.per_id = idpersona AND (p.per_fechabaja IS NULL AND p.per_razonbaja IS NULL);

$$ LANGUAGE SQL;
/*
DROP FUNCTION membresia.get_data_persona
(INOUT idpersona integer, OUT cedula varchar, OUT persona text, OUT observacion varchar,
OUT idrequisito integer, OUT requisito varchar)
*/
SELECT * FROM membresia.get_data_persona_requisito(2);