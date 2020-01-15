create or replace function actividades.gestionar_reservas(opcion varchar, resid integer, anhoid integer, eveid integer, lugid integer, perid integer, 
resfechainicio date,reshorainicio time, resfechafin date, reshorafin time, resobs text, creadoporusuario integer, modificadoporusuario integer)
returns boolean as
$$
/**
 * Procedimiento gestionar_reservas
 * Se define el CRUD para las actividades anuales
 * con opciones como:
 * registrar, modificar, cancelar, confirmar
 * Autor: Juan José González Ramírez <juanftp100@gmail.com>
 * versión 1.0
*/
declare
	v_lugar varchar;
	v_obs text := TRIM(UPPER(resobs));
	v_fechactual timestamp := now();
begin
	if opcion in ('registrar', 'modificar') then
		--Obtener descripcion de lugar.
		select lug_des into v_lugar from referenciales.lugares where lug_id = lugid;
		--Validar
		select actividades.verificar_actividadv2(v_lugar, resfechainicio, reshorainicio, resfechafin, reshorafin);
		select actividades.verifica_persona_admision(perid);
	end if;

	--Operaciones
	case opcion
		when 'registrar' then
			INSERT INTO actividades.reservas
			(anho_id, eve_id, lug_id, per_id, res_estado, res_fechainicio, res_horainicio
			, res_fechafin, res_horafin, res_obs, creado_por_usuario, creacion_fecha)
			VALUES(anhoid, eveid, lugid, perid, 'NO-CONFIRMADO', resfechainicio, reshorainicio, resfechafin, reshorafin, v_obs, creadoporusuario, v_fechactual);
			return true;
		when 'modificar' then
			UPDATE actividades.reservas
			SET eve_id=eveid, lug_id=lugid, per_id=perid, res_fechainicio=resfechainicio, res_horainicio=reshorainicio, 
			res_fechafin=resfechafin, res_horafin=reshorafin, res_obs=resobs, modificado_por_usuario=modificadoporusuario,
			modif_fecha=v_fechactual
			WHERE res_id=resid;
			return true;
		when 'cancelar' then
			UPDATE actividades.reservas
			SET res_estado='CANCELADO', modificado_por_usuario=modificadoporusuario, modif_fecha=v_fechactual
			WHERE res_id=resid;
		when 'confirmar' then
			UPDATE actividades.reservas
			SET res_estado='CONFIRMADO', modificado_por_usuario=modificadoporusuario, modif_fecha=v_fechactual
			WHERE res_id=resid;
			return true;
		else 
			raise exception 'La operacion ingresada no es valida';
			return false;
	end case;
end
$$ language plpgsql;