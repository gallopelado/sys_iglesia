CREATE OR REPLACE FUNCTION membresia.get_listapostulantes_id(idpostulacion integer)
RETURNS TABLE(
	idpostu integer	
	, descripcion text		
	, fechafin date
	, vacancias bigint
	, detalle json[]
) AS
$$
/**
* Procedimiento:get_listapostulantes_id
* Parametros: idpostulacion integer
* Descripcion: Obtiene la lista de postulante registrados segun idpostulacion.
* Autor: Juan José González Ramírez <juanftp100@gmail.com>
* Version: 1.0
* Fecha: 08-10-2019
*/
BEGIN

	RETURN QUERY SELECT 
		-- Muestra datos de cabecera.
		cp.post_id
	, cp.post_des
	, cp.post_finpostu
	, SUM(pd.cantidad) vacancias
		-- Ver el detalle.
		, ARRAY(
			SELECT
				JSON_BUILD_OBJECT( 
				'post_id', cd.post_id, 
				'candidato', p.per_nombres||' '||p.per_apellidos , 
				'fecha_creacion', to_char(cd.fecha_creacion, 'DD "de" TMMonth "del" YYYY'))
			FROM
				membresia.candi_detalle AS cd
			LEFT JOIN referenciales.personas AS p ON cd.mo_id = p.per_id
			WHERE
				cd.post_id = cp.post_id
		) detalle
	FROM
		membresia.cabe_postulacion AS cp
	LEFT JOIN membresia.postu_detalle AS pd USING(post_id)
	LEFT JOIN membresia.candi_detalle AS cd USING(post_id)
	WHERE
		post_id = idpostulacion
	GROUP BY post_id, post_des, post_finpostu;

	RETURN;	
	
END;
$$ LANGUAGE plpgsql;