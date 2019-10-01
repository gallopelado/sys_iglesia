CREATE OR REPLACE FUNCTION membresia.get_postulacion_id(idpostulacion integer)
RETURNS TABLE(
	idpostu integer
	, idministerio integer
	, ministerio varchar
	, descripcion text
	, documento TEXT
	, fechainicio date
	, fechafin date
	, detalle json[]
) AS
$$
/**
* Procedimiento:get_postulacion_id
* Parametros: idpostulacion integer
* Descripcion: Obtiene la postulacion registrada segun idpostulacion.
* Autor: Juan José González Ramírez <juanftp100@gmail.com>
* Version: 1.0
* Fecha: 08-09-2019
*/
BEGIN

	RETURN QUERY SELECT 
		-- Muestra datos de cabecera.
		cab.post_id idpostulacion
		, cab.min_id idministerio
		, m.min_des ministerio
		, cab.post_des descripcion
		, cab.post_doc documento
		, cab.post_iniciopostu fechainicio
		, cab.post_finpostu fechafin
		-- Ver el detalle.
		, ARRAY(
			SELECT 
				json_build_object(
				'post_id',post_id, 'pro_des', pro_des
				,'pro_id',pro_id, 'cantidad',cantidad)
			FROM
				membresia.postu_detalle
			LEFT JOIN referenciales.profesiones using (pro_id)
			WHERE
				post_id = cab.post_id
		) detalle
	FROM
		membresia.cabe_postulacion cab
	LEFT JOIN 
		referenciales.ministerios m using(min_id)
	WHERE
		cab.post_id = idpostulacion;

	RETURN;	
	
END;
$$ LANGUAGE plpgsql;