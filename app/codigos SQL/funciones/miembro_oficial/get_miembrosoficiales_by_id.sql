CREATE OR REPLACE FUNCTION membresia.get_miembrosoficiales_by_id(integer) 
RETURNS TABLE
(idmiembro integer, miembro TEXT, idrazonalta integer, requisito varchar,
fechaconversion text, fechabautismo text, estadom membresia.estado_membresia, 
lugarbautismo varchar, ministro varchar, fechainiciomembresia text,
bautizadoeniglesia boolean, padresmiembros boolean, recibioes boolean,
obs varchar) AS
$$
/**
 * Funcion: membresia.get_miembrosoficiales_by_id
 * Descripción: Obtiene datos del miembro oficial por id.
 * Versión: 1.0
 * Fecha: 10/08/2019
 * Autor: Juan José González Ramírez
 * Email: juanftp100@gmail.com
 */
SELECT
	mie.mo_id idmiembro,--integer
	per.per_nombres || ' ' || per.per_apellidos AS miembro,--text
	mie.razonalta_id idrazonalta,--integer
	req.req_des requisito,--varchar
	(SELECT to_char(mie.mo_fechaconversion, 'DD/MM/YYYY'::TEXT)) AS fechaconversion,--text
	(SELECT to_char(mie.mo_fechabautismo, 'DD/MM/YYYY'::TEXT)) AS fechabautismo,--text
	mie.mo_estadomembresia estadomembresia,--estadomembresia
	mie.mo_lugarbautismo lugarbautismo,--varchar
	mie.mo_oficiador ministro,--varchar
	(SELECT to_char(mie.mo_fechainiciomembresia, 'DD/MM/YYYY'::TEXT)) AS fechainiciomembresia,--text
	mie.mo_bautizadoeniglesia bautizadoeniglesia,--boolean
	mie.mo_padresmiembros padresmiembros,--boolean
	mie.mo_recibioes recibioes,---boolean
	mie.mo_obs obs--varchar
FROM
	membresia.miembros_oficiales AS mie
LEFT JOIN 
	referenciales.personas AS per ON mie.mo_id = per.per_id
LEFT JOIN
	referenciales.requisitos AS req ON mie.razonalta_id = req.req_id
WHERE
	mie.mo_id = $1;

$$ LANGUAGE SQL;

--SELECT * FROM membresia.get_miembrosoficiales_by_id(8); 


