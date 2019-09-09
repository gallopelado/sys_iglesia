CREATE OR REPLACE FUNCTION membresia.get_postulacion_id(idpostulacion integer)
RETURNS [tipo] AS
$$
/**
* Procedimiento:get_postulacion_id
* Parametros:
* Descripcion:
* Autor: Juan José González Ramírez <juanftp100@gmail.com>
* Version: 1.0
* Fecha: 08-09-2019
*/
BEGIN

	SELECT 
	-- Muestra datos de cabecera.
	cab.post_id idpostulacion
	, cab.min_id idministerio
	, m.min_des ministerio
	, cab.post_des descripcion
	, cab.post_doc documento
	-- Ver el detalle.
	, ARRAY(
		SELECT 
			json_build_object(
			'post_id',post_id, 'pro_des', pro_des
			,'pro_id',pro_id)
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
	cab.post_id = 1;

	
	

END
$$ LANGUAGE plpgsql;