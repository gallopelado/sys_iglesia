create or replace function cursos.obtener_dias_activos_segun_fecha(
	idmalla integer, vturno turno, idprofesor integer, idcurso integer, idasignatura integer, idnumeroasignatura integer
)
returns table(v_malla_id integer, v_cur_id integer, v_asi_id integer, v_num_id integer, v_per_id integer, v_cur_des text, v_asi_des text, v_num_des text, v_fecha_inicio date, v_fecha_fin date, v_dias json) as
$$
/**
 * Procedimiento: obtener_dias_activos_json
 * Autor: Juan José González Ramírez
 * Fecha creación: 2020-07-21
 * Parametros: idmalla integer, vturno turno, idprofesor integer
 * Descripción: Segun consulta se obtienen los dias activos por asignatura.
 * El formato para los dias es en formato JSON, se muestra ejemplo:
 * '{"DOMINGO":false, "LUNES":false, "MARTES":false, "MIERCOLES":false, "JUEVES":false, "VIERNES":false, "SABADO":false}'
 * version: 0.3
 */
declare
	dias json := '{"DOMINGO":false, "LUNES":false, "MARTES":false, "MIERCOLES":false, "JUEVES":false, "VIERNES":false, "SABADO":false}';
	malla_id integer;
	cur_id integer;
	asi_id integer;
	num_id integer;
	per_id integer;
	cur_des text;
	asi_des text;
	num_des text;
	fecha_inicio date;
	fecha_fin date;
	acumu varchar[];
	i integer;
begin 
		SELECT
			dp.malla_id, dp.cur_id, dp.asi_id, na.num_id, dp.per_id, c.cur_des, a.asi_des, na.num_des, dp.fechainicio, dp.fechafin, array_agg(fm.frma_dia)acum_dias 
		INTO malla_id, cur_id, asi_id, num_id, per_id, cur_des, asi_des, num_des, fecha_inicio, fecha_fin, acumu
		FROM cursos.detalle_planificacion dp
		LEFT JOIN referenciales.cursos c ON c.cur_id = dp.cur_id 
		LEFT JOIN referenciales.asignaturas a ON a.asi_id = dp.asi_id 
		LEFT JOIN referenciales.numero_asignatura na ON na.num_id = dp.num_id 
		LEFT JOIN referenciales.maestros m ON m.per_id = dp.per_id 
		LEFT JOIN referenciales.personas p ON p.per_id = m.per_id 
		LEFT JOIN cursos.malla_curricular mc ON mc.malla_id = dp.malla_id 
		INNER JOIN cursos.frecuencia_materia fm ON fm.malla_id = dp.malla_id AND fm.asi_id = dp.asi_id AND fm.num_id = dp.num_id AND fm.turno = dp.turno AND fm.cur_id = dp.cur_id 
		WHERE 
			mc.estado IS TRUE AND dp.malla_id = idmalla  AND dp.turno = vturno AND dp.per_id = idprofesor 
			AND dp.cur_id = idcurso AND dp.asi_id = idasignatura AND dp.num_id = idnumeroasignatura
		group by dp.malla_id, dp.cur_id, dp.asi_id, na.num_id, dp.per_id, c.cur_des, a.asi_des, na.num_des, dp.fechainicio, dp.fechafin;
		
		if acumu is null then
			raise exception 'Este curso no tiene dias establecidos' using ERRCODE = '10998';
		end if;
		
		for i in 1..array_upper(acumu, 1) 
		loop
			RAISE NOTICE '%', acumu[i];
			CASE acumu[i]
				WHEN 'DOMINGO' THEN
					dias := dias::jsonb - 'DOMINGO' || '{"DOMINGO":true}'::jsonb;
				WHEN 'LUNES' THEN
					dias := dias::jsonb - 'LUNES' || '{"LUNES":true}'::jsonb;
				WHEN 'MARTES' THEN
					dias := dias::jsonb - 'MARTES' || '{"MARTES":true}'::jsonb;
				WHEN 'MIERCOLES' THEN
					dias := dias::jsonb - 'MIERCOLES' || '{"MIERCOLES":true}'::jsonb;
				WHEN 'JUEVES' THEN
					dias := dias::jsonb - 'JUEVES' || '{"JUEVES":true}'::jsonb;
				WHEN 'VIERNES' THEN
					dias := dias::jsonb - 'VIERNES' || '{"VIERNES":true}'::jsonb;
				WHEN 'SABADO' THEN
					dias := dias::jsonb - 'SABADO' || '{"SABADO":true}'::jsonb;
				ELSE
					dias := dias;
			END CASE;
		end loop;
		raise notice '%', dias;
		
		drop table if exists temporal_data;
		create temp table temporal_data(v_malla_id integer, v_cur_id integer, v_asi_id integer, v_num_id integer
		, v_per_id integer, v_cur_des text, v_asi_des text, v_num_des text, v_fecha_inicio date, v_fecha_fin date, v_dias json);
		insert into temporal_data values(malla_id, cur_id, asi_id, num_id, per_id, cur_des, asi_des, num_des, fecha_inicio, fecha_fin, dias);
		
		return query select * from temporal_data;
end
$$ language plpgsql;