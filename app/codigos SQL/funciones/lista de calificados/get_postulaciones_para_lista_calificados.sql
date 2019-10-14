CREATE OR REPLACE FUNCTION membresia.get_postulaciones_para_lista_calificados()
RETURNS TABLE(idpostulacion integer, postulacion TEXT, estado TEXT, cantidad_postulantes bigint) as
$$
/**
 * Funcion: get_postulaciones_para_lista_calificados
 * 
 * Obtiene aquellas postulaciones que cumplieron la fecha de finalización y
 * tiene candidatos a evaluarse.
 * Autor: Juan José González Ramírez <juanftp100@gmail.com>
 * Fecha: 13-10-2019
 */
SELECT 
	cp.post_id idpostulacion
	, cp.post_des postulacion
	, (CASE  WHEN cp.post_fechacalificado IS NULL THEN 'ACTIVO' WHEN cp.post_fechacalificado IS NOT NULL THEN 'PROCESADO' END) AS estado
	, (SELECT count(*) FROM membresia.candi_detalle cd WHERE cd.post_id = cp.post_id) AS cantidad_postulantes	
FROM
	membresia.cabe_postulacion AS cp
WHERE 
	-- Cuando el estado de la postulacion es false con fecha de procesado, indica que esta lista para
	-- calificarse, esta cerrada.
	cp.post_estado IS FALSE AND cp.post_fechaprocesado IS NOT NULL
	-- Solamente aquellas postulaciones con candidatos.
	AND (SELECT count(*) FROM membresia.candi_detalle cd WHERE cd.post_id = cp.post_id) > 0;

$$ LANGUAGE sql;

--SELECT membresia.get_postulaciones_para_lista_calificados();