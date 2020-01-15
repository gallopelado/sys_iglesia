create or replace function actividades.verificar_actividadv2(lugar text, fechaini date, horaini time, fechafin date, horafin time)
returns boolean as
$$
/*
 * Funcion verificar_actividadv2
 * Se encarga de verificar segun fechas y horas ingresadas
 * donde no deben superponerse las actividades y reservas de un mismo lugar.
 * Autor: Juan Jose Gonzalez Ramirez <juanftp100@gmail.com>
 * Fecha: 14-01-2020
 * version: 2.0
*/
declare		
	bandera boolean := false;
	s_fechainicio DATE := fechaini;
	s_horainicio  TIME := horaini;
	-----
	s_fechafin DATE := fechafin;
	s_horafin TIME := horafin;
	-----
	v_fechainicio TIMESTAMP := concat(s_fechainicio,' ', s_horainicio)::timestamp;
	v_fechafin TIMESTAMP := concat(s_fechafin,' ', s_horafin)::timestamp;
	-----
	v_anhohabil integer := (select anho_des from referenciales.anho_habil where is_active = true);
	
begin
	--control de actividades
	perform 
		lug_des,
		concat(act_fechainicio,' ',act_horainicio)::timestamp fechainicio,
		concat(act_fechafin, ' ', act_horafin)::timestamp fechafin
	from actividades.actividades
	left join referenciales.lugares using(lug_id)
	where 
	((v_fechainicio between concat(act_fechainicio,' ',act_horainicio)::timestamp and concat(act_fechafin, ' ', act_horafin)::timestamp)
	or
	(v_fechafin between concat(act_fechainicio,' ',act_horainicio)::timestamp and concat(act_fechafin, ' ', act_horafin)::timestamp)) and
	lug_des = lugar;
	if not found then
		raise notice 'Es posible registrar esta actividad';
		bandera := true;
	else
		raise exception 'No es posible registrar esta actividad';
		return bandera;
	end if;

	--control de reservas
	if bandera is true then
		perform 
			lug_des,
			concat(res_fechainicio,' ',res_horainicio)::timestamp fechainicio,
			concat(res_fechafin, ' ', res_horafin)::timestamp fechafin
		from actividades.reservas
		left join referenciales.lugares using(lug_id)
		where 
		((v_fechainicio between concat(res_fechainicio,' ',res_horainicio)::timestamp and concat(res_fechafin, ' ', res_horafin)::timestamp)
		or
		(v_fechafin between concat(res_fechainicio,' ',res_horainicio)::timestamp and concat(res_fechafin, ' ', res_horafin)::timestamp)) and
		lug_des = lugar;
		if not found then
			raise notice 'Es posible registrar esta reserva';
			return true;
		else
			raise exception 'No es posible registrar esta reserva';
			return false;
		end if;
	end if;
	
end
$$ language plpgsql; 