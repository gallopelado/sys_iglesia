create or replace procedure membresia.gestionar_actividades_anuales(
	opcion varchar, anhohabil integer, eveid integer, lugid integer, actfecha date, 
	acthora time, plazid integer, actrepite boolean, actobs text, minid integer, creadoporusuario integer
) language plpgsql as $$
/**
 * Procedimiento gestionar_actividades_anuales
 * Se define el CRUD para las actividades anuales
 * con opciones como:
 * registrar, modificar, eliminar, repetir_por_año
 * Autor: Juan José González Ramírez <juanftp100@gmail.com>
 * versión 1.0
*/
DECLARE
	v_actobs TEXT := TRIM(UPPER(actobs));
	fecha_actual TIMESTAMP := now();	
begin
	CASE opcion
		WHEN 'registrar' THEN
			INSERT INTO actividades.actividades(
				anho_habil
				, eve_id
				, lug_id
				, act_fecha
				, act_hora
				, plaz_id
				, act_repite
				, act_obs
				, min_id
				, creado_por_usuario
				, creacion_fecha
				, modificado_por_usuario
				, modif_fecha
			)
			VALUES (
				anhohabil
				, eveid
				, lugid
				, actfecha
				, acthora
				, plazid
				, actrepite
				, v_actobs
				, minid
				, creadoporusuario
				, fecha_actual
				, NULL
				, NULL
			);
			raise notice 'Actividad registrada';
		WHEN 'modificar' THEN
			UPDATE actividades.actividades
			SET 								
				lug_id = lugid
				, act_fecha=?
				, act_hora=?
				, plaz_id=?
				, act_repite=?
				, act_obs=?
				, min_id=?
				, creado_por_usuario=?
				, creacion_fecha=?
				, modificado_por_usuario=?
				, modif_fecha=?
			WHERE anho_habil = anhohabil AND eve_id = eveid;
		WHEN 'eliminar' THEN
		WHEN 'repetir_por_año' THEN
	END CASE;
end
$$;