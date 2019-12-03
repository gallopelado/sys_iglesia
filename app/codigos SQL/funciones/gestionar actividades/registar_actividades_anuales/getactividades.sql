create or replace function actividades.get_actividades(integer)
returns table(
	act_id idactividad
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
) as
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
left join referenciales.ministerios using(min_id);