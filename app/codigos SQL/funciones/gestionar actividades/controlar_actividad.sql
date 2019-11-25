-- Validacion cuando se quiere utilizar el mismo lugar con las mismas fechas
do $$
declare
	item RECORD;
	actividades CURSOR FOR 
		SELECT * 
		FROM actividades.actividades
		LEFT JOIN referenciales.anho_habil USING(anho_id)
		LEFT JOIN referenciales.eventos USING(eve_id)
		LEFT JOIN referenciales.lugares USING(lug_id)
		LEFT JOIN referenciales.plazos USING(plaz_id)
		LEFT JOIN referenciales.ministerios USING(min_id);
	--v_lugar varchar := 'SALON PRINCIPAL';
	--v_lugar varchar := 'RANCHO ALEGRE';
	v_lugar varchar := 'OFICINA PASTORAL';
	v_fechainicio date := '2019-07-22';
	v_horainicio time := '16:00';
	
	v_fechafin date := '2019-07-25';
	v_horafin time := '15:00';
begin
	-- Recorrer conjunto de datos.
	for item in actividades 
	loop
		/*raise notice 'fechainicio/hora % y fechafin/hora % , Lugar de reunion: %', 
		item.act_fechainicio::text||' '||item.act_horainicio::text, 
		item.act_fechafin::text ||' '||item.act_horafin, 
		item.lug_des;*/
		
		--Validaciones
		--Si se quiere controlar cuando se escoge el mismo lugar.
		if v_lugar = item.lug_des then
			--Cuando es todo el dia.
			
			raise notice 'v_fechainicio %, item.act_fechainicio % ... v_fechafin %, item.act_fechafin %', 
			v_fechainicio, item.act_fechainicio, v_fechafin, item.act_fechafin;
			
			-- Caso cuando es el mismo día
			if v_fechainicio = v_fechafin then
				raise notice 'Opcion en el mismo día';
				if v_fechainicio = item.act_fechainicio and v_fechafin = item.act_fechafin then
					if v_horainicio = item.act_horainicio and v_horafin = item.act_horafin then
						raise exception 'En este día y horas ya existe una actividad';
					end if;
					if v_horainicio < v_horafin then
						if v_horainicio > item.act_horainicio and v_horainicio > item.act_horafin and v_horafin >  item.act_horafin then
							raise notice 'Registrando actividad mismo_dia__01';
						elsif v_horainicio < item.act_horainicio and v_horainicio < item.act_horafin and v_horafin < item.act_horainicio and v_horafin < item.act_horafin then
							raise notice 'Registrando actividad mismo_dia__02';						
						end if;
					else
						raise exception 'Debe ingresar hora final mayor que la hora inicial';
					end if;
				end if;
			elsif v_fechainicio < v_fechafin then
				raise notice 'Opcion más días';
				if v_fechainicio = item.act_fechainicio and v_fechafin = item.act_fechafin then
					raise exception 'Ya esta reservada una actividad en estas fechas y horas';
				elsif v_fechainicio > item.act_fechainicio and v_fechafin > item.act_fechafin then
					raise notice 'Registrando actividad mas_dias__01';
				elsif v_fechainicio < item.act_fechainicio and v_fechafin < item.act_fechafin and v_fechafin < item.act_fechainicio then
					raise notice 'Registrando actividad mas_dias__02';
				else
					raise exception 'Existe una reserva activa';
				end if;
			end if;
		else --Cuando no es el mismo lugar
			raise notice 'Realizar insert de actividad cuando no coincide el lugar';
		end if;--if principal
	end loop;--fin del ciclo for	
	
end
$$ language plpgsql;