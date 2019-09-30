CREATE OR REPLACE FUNCTION membresia.getall_postulacion()
RETURNS TABLE(idpostulacion integer, descripcion text, fechainicio varchar, fechafin varchar) AS
$$
/**
* Funcion getall_postulacion
* 
* Obtiene todas las postulaciones activas y sin  fecha de procesado.
* Autor: Juan José González Ramírez <juanftp100@gmail.com>
* versión: 1
*/

	SELECT 
		post_id
		, post_des
		, fecha_formatolargo(post_iniciopostu) fechainicio
		, fecha_formatolargo(post_finpostu)	fechafin				
	FROM 
		membresia.cabe_postulacion
	WHERE
		post_estado = TRUE AND post_fechaprocesado IS NULL;
		
$$ LANGUAGE sql;

SELECT * FROM membresia.getall_postulacion();