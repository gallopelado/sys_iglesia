CREATE OR REPLACE FUNCTION membresia.get_postulacion_id(idpostulacion integer)
RETURNS [tipo] AS
$
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
		post_id AS idpostulacion
		, min_id AS idministerio
		, post_des AS descripcion
		, post_doc AS documento
		, post_iniciopostu AS fechainicio
		, post_finpostu AS fechafin
	FROM 
		membresia.cabe_postulacion
	
	WHERE post_id = idpostulacion;
	

END
$ LANGUAGE plpgsql;