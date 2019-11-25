create or replace function actividades.verificar_actividad(lugar text, fechaini date, horaini time, fechafin date, horafin time)
returns boolean as
$$
/*
 * Funcion verificar_actividad
 * Se encarga de verificar segun fechas y horas ingresadas
 * donde no deben superponerse las actividades de un mismo lugar.
 * Autor: Juan Jose Gonzalez Ramirez <juanftp100@gmail.com>
 * Fecha: 25-11-2019
 * version: 1.0
*/
declare
	v_lugar text := lugar;
	v_fechainicio date := fechaini;
	v_horainicio time := horaini;	
	v_fechafin date := fechafin;
	v_horafin time := horafin;
	item RECORD;
	actividades CURSOR FOR SELECT * FROM actividades.actividades
	LEFT JOIN referenciales.anho_habil USING(anho_id)
	LEFT JOIN referenciales.eventos USING(eve_id)
	LEFT JOIN referenciales.lugares USING(lug_id)
	LEFT JOIN referenciales.plazos USING(plaz_id)
	LEFT JOIN referenciales.ministerios USING(min_id);		
begin
	-- Recorrer conjunto de datos.
	for item in actividades 
	loop						
		--Si se quiere controlar cuando se escoge el mismo lugar.
		if v_lugar = item.lug_des then			
			-- Caso cuando es el mismo día
			if v_fechainicio = v_fechafin then				
				if v_fechainicio = item.act_fechainicio and v_fechafin = item.act_fechafin then
					if v_horainicio = item.act_horainicio and v_horafin = item.act_horafin then
						return false;
					end if;
					if v_horainicio < v_horafin then
						if v_horainicio > item.act_horainicio and v_horainicio > item.act_horafin and v_horafin >  item.act_horafin then
							return true;
						elsif v_horainicio < item.act_horainicio and v_horainicio < item.act_horafin and v_horafin < item.act_horainicio and v_horafin < item.act_horafin then
							return true;
						end if;
					else
						return false;
					end if;
				end if;
			elsif v_fechainicio < v_fechafin then				
				if v_fechainicio = item.act_fechainicio and v_fechafin = item.act_fechafin then
					return false;
				elsif v_fechainicio > item.act_fechainicio and v_fechafin > item.act_fechafin then
					return true;
				elsif v_fechainicio < item.act_fechainicio and v_fechafin < item.act_fechafin and v_fechafin < item.act_fechainicio then
					return true;
				else
					return false;
				end if;
			end if;
		else --Cuando no es el mismo lugar
			return true;
		end if;--if principal
	end loop;--fin del ciclo for
end
$$ language plpgsql;