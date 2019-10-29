CREATE OR REPLACE PROCEDURE membresia.gestionar_obreros(
	opcion varchar, idcomite integer, idpersona integer, idpostulacion integer
	, entrena boolean, obs TEXT, motivo_baja TEXT, motivo_reincorporacion TEXT, idusuario integer
) LANGUAGE plpgsql AS $$
/*
 * Procedimiento gestionar obreros
 * Se define según las operaciones
 * registrar, modificar, baja, reincorporar
 * de los obreros para los comités.
 * Autor: Juan José González Ramírez <juanftp100@gmail.com>
 * Versión: 0.1
 * 
 */
DECLARE
	v_obs TEXT := TRIM(upper(obs));
	v_actual date:= now();
	v_motivo_baja TEXT := TRIM(UPPER(motivo_baja));
	v_motivo_reincorporacion TEXT := TRIM(UPPER(motivo_reincorporacion));
BEGIN
	-- Verificar si esta en candi_admitidos.
	SELECT membresia.verifica_admitido(idpersona, idpostulacion);
	-- Casos
	CASE opcion
		WHEN 'registrar' THEN						
			INSERT INTO membresia.comite_obreros(min_id, per_id, fecha_ingreso, entrenamiento, observacion, estado, creado_por_usuario)
			VALUES (idcomite, idpersona, v_actual, entrena, v_obs, TRUE, NULL);
			RAISE NOTICE 'Se registró con exito un nuevo obrero';
		WHEN 'modificar' THEN			
			UPDATE membresia.comite_obreros SET entrenamiento = entrena, observacion = v_obs
			WHERE min_id = idcomite AND per_id = idpersona;
			RAISE NOTICE 'Se actualizó con exito el obrero';
		WHEN 'baja' THEN			
			IF v_motivo_baja IS NOT NULL THEN
				UPDATE membresia.comite_obreros SET estado = FALSE, 
					motivo_baja = v_motivo_baja || ' -FECHA(' || v_actual || ')'
				WHERE min_id = idcomite AND per_id = idpersona;
				RAISE NOTICE 'Se ha dado de baja el obrero';	
			ELSE
				RAISE EXCEPTION 'Debe cargar el motivo de la baja' USING ERRCODE='20100';
			END IF;
		WHEN 'reincorporar' THEN
			IF v_motivo_reincorporacion IS NOT NULL THEN
				UPDATE membresia.comite_obreros SET motivo_reincorporacion = v_motivo_reincorporacion|| ' -FECHA(' || v_actual || ')',
					motivo_baja = NULL, estado = TRUE
				WHERE min_id = idcomite AND per_id = idpersona;
				RAISE NOTICE 'Se ha reactivado el obrero';
			ELSE
				RAISE EXCEPTION 'Debe cargar el motivo de la reincorporación' USING ERRCODE = '20101';
			END IF;
		ELSE
			RAISE EXCEPTION 'Ninguna opción es correcta.' USING ERRCODE='20099';
	END CASE;
END
$$;