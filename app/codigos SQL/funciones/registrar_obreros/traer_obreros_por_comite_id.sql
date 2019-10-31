CREATE OR REPLACE FUNCTION membresia.traer_obreros_por_comite_id(integer, integer)
RETURNS table(idcomite integer, idpersona integer, obrero TEXT, fechaingreso TEXT, entrenamiento TEXT, observacion text) AS
$$

SELECT 
	co.min_id idcomite
	, co.per_id idpersona
	, per_nombres || ' ' ||per_apellidos obrero
	, fecha_formatolargo(co.fecha_ingreso)fechaingreso
	, (CASE co.entrenamiento WHEN TRUE THEN 'SI' WHEN FALSE THEN 'NO' END) entrenamiento
	, co.observacion
FROM
	membresia.comite_obreros AS co
LEFT JOIN referenciales.personas using(per_id)
WHERE min_id = $1 AND per_id = $2;

$$ LANGUAGE SQL;

SELECT * FROM membresia.traer_obreros_por_comite_id(3,8)