create or replace procedure actividades.gestionar_actividades_anuales(
	opcion varchar, id integer, anhohabil integer, eveid integer, lugid integer, 
	fechaini date, horaini time, fechafin date, horafin time, plazid integer, 
	actrepite boolean, actobs text, minid integer, creadoporusuario integer
) language plpgsql as $$
/**
 * Procedimiento gestionar_actividades_anuales
 * Se define el CRUD para las actividades anuales
 * con opciones como:
 * registrar, modificar, eliminar, repetir_por_año
 * Autor: Juan José González Ramírez <juanftp100@gmail.com>
 * versión 1.4
*/
DECLARE
	v_actobs TEXT := TRIM(UPPER(actobs));	
	fecha_actual TIMESTAMP := now();
	v_anho integer;
	v_lugar text;
	actividades refcursor;
	reg record;
	v_fechaini date;
	v_horaini time;
	v_fechafin date;
	v_horafin time;
	
begin
	if opcion != 'repetir_por_año' then
		-- Validar año habil.
		select anho_id into v_anho from referenciales.anho_habil where anho_des = anhohabil and is_active = TRUE;
		if not found THEN
			raise exception 'Este año no esta habilitado' using ERRCODE = '20500';
		end if;
	end if;
	
	if opcion IN ('registrar', 'modificar') then
		--Obtener descripcion de lugar.
		select lug_des into v_lugar from referenciales.lugares where lug_id = lugid;
		if not found THEN
			raise exception 'Este lugar no parece valido' using ERRCODE = '20501';
		end if;
	end if;

	CASE opcion
		WHEN 'registrar' THEN
			if actividades.verificar_actividad(v_lugar, fechaini, horaini, fechafin, horafin) is TRUE THEN
				INSERT INTO actividades.actividades
				(					
					anho_id
					, eve_id
					, lug_id
					, act_fechainicio
					, act_horainicio
					, act_fechafin
					, act_horafin
					, plaz_id
					, act_repite
					, act_obs
					, min_id
					, creado_por_usuario
					, creacion_fecha
					, modificado_por_usuario
					, modif_fecha
				)
				VALUES 
					( 
						v_anho
						, eveid
						, lugid
						, fechaini
						, horaini
						, fechafin
						, horafin
						, plazid
						, actrepite
						, v_actobs
						, minid
						, creadoporusuario
						, fecha_actual
						, NULL
						, NULL
					);
				raise notice 'Se inserto correctamente el registro actividad';
			ELSE
				raise exception 'Quiza existe una actividad en dichas fechas' using ERRCODE = '20600';
			end if;
		WHEN 'modificar' THEN
			--Obtener dicho registro para comparar fechas
			SELECT act_fechainicio, act_horainicio, act_fechafin, act_horafin 
			into v_fechaini, v_horaini, v_fechafin, v_horafin
			FROM actividades.actividades WHERE act_id = id; 
			--raise notice 'fechaini=%, v_fechaini=%, horaini=%, v_horaini=%, fechafin=%, v_fechafin=%, horafin=%, v_horafin=%', fechaini,v_fechaini,horaini,v_horaini,fechafin,v_fechafin,horafin,v_horafin;
			if (fechaini = v_fechaini and horaini = v_horaini) and (fechafin = v_fechafin and horafin = v_horafin) then
				--raise notice 'FECHAS IGUALES';				
				UPDATE actividades.actividades
					SET 
						anho_id = v_anho
						, eve_id = eveid
						, lug_id = lugid
						, act_fechainicio = fechaini
						, act_horainicio = horaini
						, act_fechafin = fechafin
						, act_horafin = horafin
						, plaz_id = plazid
						, act_repite = actrepite
						, act_obs = v_actobs
						, min_id = minid
						, modificado_por_usuario = creadoporusuario
						, modif_fecha = fecha_actual
					WHERE act_id = id;				
			ELSE
				--raise notice 'FECHAS NO IGUALES';
				if actividades.verificar_actividad(v_lugar, fechaini, horaini, fechafin, horafin) is TRUE THEN
					UPDATE actividades.actividades
					SET 
						anho_id = v_anho
						, eve_id = eveid
						, lug_id = lugid
						, act_fechainicio = fechaini
						, act_horainicio = horaini
						, act_fechafin = fechafin
						, act_horafin = horafin
						, plaz_id = plazid
						, act_repite = actrepite
						, act_obs = v_actobs
						, min_id = minid
						, modificado_por_usuario = creadoporusuario
						, modif_fecha = fecha_actual
					WHERE act_id = id;
					raise notice 'Se modifico correctamente el registro actividad';
				ELSE
					raise exception 'Quiza existe una actividad en dichas fechas' using ERRCODE = '20600';
				end if;
			end if;
		WHEN 'eliminar' THEN
			-- Solo puede eliminarse registros que pertenecen al año actual, no menores al él.
			if anhohabil >= EXTRACT(year from fecha_actual) THEN
				delete from actividades.actividades
				where act_id = id;
			ELSE
				raise exception 'No se ha podido eliminar el registro actividad' using ERRCODE = '20601';
			end if;
		WHEN 'repetir_por_año' THEN
			/*
			* Hacer la insercion en masa de la coleccion cuyo atributo act_repite es true,
			* con la condicion de que el año actual se le sume 1. Esta opcion se realiza el ultimo 
			* dia del año o cuando se habilite el año habil para la programacion adelantada.
			*/
			open actividades for select * from actividades.actividades;
			if anhohabil = extract(year from fecha_actual) THEN
				anhohabil := anhohabil + 1;
				select anho_id into v_anho from referenciales.anho_habil where anho_des = anhohabil and is_active = FALSE and adelantar = TRUE;
				if not found THEN
					raise exception 'Todavía no se agregó este año = % al sistema', anhohabil;
				end if;
				loop
					fetch actividades into reg;
					exit when not found;
					if reg.act_repite is true THEN
						INSERT INTO actividades.actividades
							(					
								anho_id
								, eve_id
								, lug_id
								, act_fechainicio
								, act_horainicio
								, act_fechafin
								, act_horafin
								, plaz_id
								, act_repite
								, act_obs
								, min_id
								, creado_por_usuario
								, creacion_fecha
								, modificado_por_usuario
								, modif_fecha
							)
						VALUES 
							( 
								v_anho
								, reg.eve_id
								, reg.lug_id
								, (select (reg.act_fechainicio + interval '1 year')::date)
								, reg.act_horainicio
								, (select (reg.act_fechafin + interval '1 year')::date)
								, reg.act_horafin
								, reg.plaz_id
								, reg.act_repite
								, reg.act_obs
								, reg.min_id
								, creadoporusuario
								, fecha_actual
								, NULL
								, NULL
							);
					end if;
				end loop;
			end if;
			close actividades;
	END CASE;
end
$$;