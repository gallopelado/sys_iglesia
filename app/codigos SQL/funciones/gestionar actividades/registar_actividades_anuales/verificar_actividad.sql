create or replace function actividades.verificar_actividad(lugar text, fechaini date, horaini time, fechafin date, horafin time)
returns boolean as
$$
/*
 * Funcion verificar_actividad
 * Se encarga de verificar segun fechas y horas ingresadas
 * donde no deben superponerse las actividades de un mismo lugar.
 * Autor: Juan Jose Gonzalez Ramirez <juanftp100@gmail.com>
 * Fecha: 26-12-2019
 * version: 1.1
*/
declare		
	s_fechainicio DATE := fechaini;
	s_horainicio  TIME := horaini;
	-----
	s_fechafin DATE := fechafin;
	s_horafin TIME := horafin;
	-----
	v_fechainicio TIMESTAMP := concat(s_fechainicio,' ', s_horainicio)::timestamp;
	v_fechafin TIMESTAMP := concat(s_fechafin,' ', s_horafin)::timestamp;
	-----
	model_fechainicio TIMESTAMP;
	model_fechafin TIMESTAMP;
	model_s_fechainicio DATE;
	model_s_horainicio TIME;
	model_s_fechafin DATE;
	model_s_horafin TIME;
	item RECORD;
	actividades CURSOR FOR SELECT * FROM actividades.actividades
	LEFT JOIN referenciales.anho_habil USING(anho_id)
	LEFT JOIN referenciales.eventos USING(eve_id)
	LEFT JOIN referenciales.lugares USING(lug_id)
	LEFT JOIN referenciales.plazos USING(plaz_id)
	LEFT JOIN referenciales.ministerios USING(min_id)
	where lug_des = lugar;	
begin
	for item in actividades 				
	loop	
		--raise notice 'Entro al 1er ciclo';
		--Asignacionde fechas		
		model_s_fechainicio := item.act_fechainicio;
		model_s_horainicio := item.act_horainicio;
		model_s_fechafin := item.act_fechafin;
		model_s_horafin := item.act_horafin;
		
		-- El dia coincide.
		if s_fechainicio = model_s_fechainicio and s_fechafin = model_s_fechafin then			
			--Analizar horas
			-- La hora de inicio y fin coinciden.
			if s_horainicio = model_s_horainicio and s_horafin = model_s_horafin then
				raise exception 'Fecha/hora reservada iguales';
				return FALSE;
			elsif s_horainicio > model_s_horainicio and s_horainicio < model_s_horafin then
				raise exception 'Hora de inicio en medio de una reserva no permitida';
				return FALSE;
			elsif s_horafin > model_s_horainicio and s_horafin < model_s_horafin then
				raise exception 'Hora de fin en medio de una reserva no permitida';
				return FALSE;
			elsif s_horainicio = model_s_horainicio and s_horainicio < model_s_horafin then
				raise exception 'Hora de inicio es igual al inicial pero sigue estando en medio';
				return FALSE;
			elsif s_horafin = model_s_horainicio and s_horafin < model_s_horafin then
				raise exception 'Hora de fin es igual al inicial pero sigue estando en medio';
				return FALSE;
			elsif s_horainicio < model_s_horainicio and s_horafin < model_s_horainicio then
				raise notice 'Evento registrado en el dia';
				return TRUE;
			elsif s_horainicio > model_s_horainicio and s_horainicio > model_s_horafin then
				raise notice 'Evento registrado en el dia2';			
				return TRUE;
			end if;			
		end if;
		
	end loop;
	--segundo loop
	for item in actividades 				
	loop	
		--Asignacionde fechas
		model_fechainicio := concat(item.act_fechainicio,' ', item.act_horainicio)::timestamp;
		model_fechafin := concat(item.act_fechafin,' ', item.act_horafin)::timestamp;
		
		if v_fechainicio > model_fechainicio and v_fechainicio > model_fechafin and v_fechafin > model_fechainicio and v_fechafin > model_fechafin then
			raise notice 'Se puede reservar a la derecha %, %',v_fechainicio, model_fechainicio;
			return TRUE;
		elsif v_fechainicio < model_fechainicio and v_fechainicio < model_fechafin and v_fechafin < model_fechainicio then
			raise notice 'Se puede reservar a la izquierda';
			return TRUE;
		else
			raise exception 'error al registrar, Ya existe reserva en medio';
			return FALSE;
		end if;
		
	end loop;
	--tercer loop
	for item in actividades 				
	loop	
		--Asignacionde fechas
		model_fechainicio := concat(item.act_fechainicio,' ', item.act_horainicio)::timestamp;
		model_fechafin := concat(item.act_fechafin,' ', item.act_horafin)::timestamp;
		
		if v_fechainicio < model_fechainicio and v_fechainicio < model_fechafin and v_fechafin < model_fechainicio then
			raise notice 'Se puede reservar a la izquierda';
			return TRUE;
		end if;
		
	end loop;
	
end
$$ language plpgsql;