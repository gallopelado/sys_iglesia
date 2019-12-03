create or replace function actividades.get_actividades(integer)
returns table(
	 idactividad integer
	,  idanho integer
	,  anho integer
	,  idevento integer
	,  evento varchar
	,  idlugar integer
	,  lugar varchar
	,  fechainicio date
	,  horainicio time
	,  fechafin date
	,  horafin time
	,  idplazo integer
	,  plazo varchar
	,  serepite boolean
	,  obs varchar
	,  idministerio integer
	,  ministerio varchar
	, creado_por_usuario integer
	, creacion_fecha timestamp
	, modificado_por_usuario integer
	, modif_fecha timestamp
) AS $$
SELECT act_id idactividad
	, anho_id idanho
	, anho_des anho
	, eve_id idevento
	, eve_des evento 
	, lug_id idlugar
	, lug_des lugar
	, act_fechainicio fechainicio
	, act_horainicio horainicio
	, act_fechafin fechafin
	, act_horafin horafin
	, plaz_id idplazo
	, plaz_des plazo
	, act_repite serepite
	, act_obs obs
	, min_id idministerio
	, min_des ministerio
	, creado_por_usuario
	, creacion_fecha
	, modificado_por_usuario
	, modif_fecha
FROM actividades.actividades
left join referenciales.anho_habil using(anho_id)
left join referenciales.eventos using (eve_id)
left join referenciales.lugares using(lug_id)
left join referenciales.plazos using(plaz_id)
left join referenciales.ministerios using(min_id)
WHERE 
	CASE WHEN $1 IS NOT NULL THEN
		 anho_des = $1
		ELSE
		anho_des IS NOT NULL
	END;
$$ LANGUAGE SQL;

--SELECT actividades.get_actividades(2018);
--DROP FUNCTION actividades.get_actividades(integer);


