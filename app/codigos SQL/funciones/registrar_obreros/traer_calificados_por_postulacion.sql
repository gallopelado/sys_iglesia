CREATE OR REPLACE FUNCTION membresia.traer_calificados_por_postulacion(idpostulacion integer)
RETURNS json AS
$$

SELECT
	array_to_json(array_agg(row_to_json(datos)))resultados
FROM (
		SELECT 
		cp.post_id	
		, ca.mo_id idmiembro
		, p.per_nombres || ' ' || p.per_apellidos miembro
		FROM 
			membresia.cabe_postulacion AS cp 
		LEFT JOIN 
			membresia.candi_admitidos AS ca ON cp.post_id = ca.post_id
		LEFT JOIN
			referenciales.personas AS p ON ca.mo_id = p.per_id
		WHERE 
			post_fechacalificado IS NOT NULL AND cp.post_id = idpostulacion

)datos;

$$ LANGUAGE sql;


SELECT membresia.traer_calificados_por_postulacion(2);