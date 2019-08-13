CREATE OR REPLACE FUNCTION membresia.get_miembros_vistaprincipal() 
RETURNS TABLE
(idmiembro integer, miembro TEXT, fechainiciomembresia date, estado membresia.estado_membresia,
idrazonalta integer, requisito varchar) AS
$$

SELECT
	mie.mo_id idmiembro,
	per.per_nombres || ' ' || per.per_apellidos AS miembro,
	mie.mo_fechainiciomembresia,
	mie.mo_estadomembresia estado,
	mie.razonalta_id idrazonalta,
	req.req_des requisito
FROM
	membresia.miembros_oficiales AS mie
LEFT JOIN 
	referenciales.personas AS per ON mie.mo_id = per.per_id
LEFT JOIN
	referenciales.requisitos AS req ON mie.razonalta_id = req.req_id
WHERE
	per.per_razonbaja IS NULL;

$$ LANGUAGE SQL;

--SELECT * FROM membresia.get_miembros_vistaprincipal();