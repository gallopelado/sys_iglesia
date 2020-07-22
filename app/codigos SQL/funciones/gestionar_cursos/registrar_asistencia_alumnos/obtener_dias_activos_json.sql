create or replace function cursos.obtener_dias_activos_json(idmalla integer, vturno turno, idprofesor integer)
returns json as
$$
/**
 * Procedimiento: obtener_dias_activos_json
 * Autor: Juan José González Ramírez
 * Fecha creación: 2020-07-21
 * Parametros: idmalla integer, vturno turno, idprofesor integer
 * Descripción: Segun consulta se obtiene en formato json los dias activos por asignatura.
 * El formato para los dias es en formato JSON, se muestra ejemplo:
 * '{"DOMINGO":false, "LUNES":false, "MARTES":false, "MIERCOLES":false, "JUEVES":false, "VIERNES":false, "SABADO":false}'
 * 
 */
declare
	dias json := '{"DOMINGO":false, "LUNES":false, "MARTES":false, "MIERCOLES":false, "JUEVES":false, "VIERNES":false, "SABADO":false}';
	acumu varchar[];
	i integer;
begin 
		SELECT
			array_agg(fm.frma_dia) 
		INTO acumu
		FROM cursos.detalle_planificacion dp
		LEFT JOIN referenciales.cursos c ON c.cur_id = dp.cur_id 
		LEFT JOIN referenciales.asignaturas a ON a.asi_id = dp.asi_id 
		LEFT JOIN referenciales.numero_asignatura na ON na.num_id = dp.num_id 
		LEFT JOIN referenciales.maestros m ON m.per_id = dp.per_id 
		LEFT JOIN referenciales.personas p ON p.per_id = m.per_id 
		LEFT JOIN cursos.malla_curricular mc ON mc.malla_id = dp.malla_id 
		INNER JOIN cursos.frecuencia_materia fm ON fm.malla_id = dp.malla_id AND fm.asi_id = dp.asi_id AND fm.num_id = dp.num_id AND fm.turno = dp.turno AND fm.cur_id = dp.cur_id 
		WHERE mc.estado IS TRUE AND dp.malla_id = idmalla  AND dp.turno = vturno AND dp.per_id = idprofesor;
		
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
		return dias;
end
$$ language plpgsql;