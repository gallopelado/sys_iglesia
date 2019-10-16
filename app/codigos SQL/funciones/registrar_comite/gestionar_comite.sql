CREATE OR REPLACE PROCEDURE membresia.gestionar_comite(
	op varchar, idministerio integer, idlider integer, idsuplente integer,
	descripcion TEXT, observacion TEXT, creadoporusuario integer
) LANGUAGE plpgsql AS $$
/**
* Procedimiento: gestionar_comite.
* Descripcion: Se definen las operaciones de:
* 'registrar' - registrar comite
* 'modificar' - modificar comite
* 'baja' - dar de baja comite
* 'reactivar' - reactivar comite
*
* Autor: Juan José González Ramírez <juanftp100@gmail.com>
* Versión: 1.0
* 
*/
DECLARE
	v_op varchar := trim(op);
	v_descripcion TEXT := trim(UPPER(descripcion));
	v_observacion TEXT := trim(UPPER(observacion));	
	v_fecha_actual date := current_date;
BEGIN
	
	-- Comprobar si existe ministerio.
	PERFORM min_id FROM referenciales.ministerios WHERE min_id = idministerio;
	IF NOT FOUND THEN
		RAISE EXCEPTION 'No existe dicho ministerio' USING ERRCODE = '20100';
	END IF;

	-- Comprobar si el lider no esta dado de baja.
	PERFORM per_id FROM referenciales.personas WHERE per_id = idlider AND per_fechabaja IS NULL AND per_razonbaja IS NULL;
	IF NOT FOUND THEN
		RAISE EXCEPTION 'No existe esta persona' USING ERRCODE = '20101';
	END IF;

	-- Comprobar suplente no esta dado de baja.
	IF idsuplente IS NOT NULL THEN
		PERFORM per_id FROM referenciales.personas WHERE per_id = idsuplente AND per_fechabaja IS NULL AND per_razonbaja IS NULL;
		IF NOT FOUND THEN
			RAISE EXCEPTION 'No existe esta persona' USING ERRCODE = '20102';
		END IF;	
	END IF;

	IF v_descripcion = '' THEN
		RAISE EXCEPTION 'No puede estar vacía la descripción' USING ERRCODE = '20103';
	END IF;
	
	-- Casos.
	CASE v_op
		WHEN 'registrar' THEN
			INSERT INTO membresia.comites(
				min_id
				, lider_id
				, suplente_id
				, com_des
				, com_obs
				, com_fechainicio
				, com_estado
				, creado_por_usuario) 
			VALUES (
				idministerio
				, idlider
				, idsuplente
				, descripcion
				, observacion
				, v_fecha_actual
				, TRUE
				, NULL
			);
			RAISE NOTICE 'Comite agregado';
		WHEN 'modificar' THEN
			UPDATE membresia.comites
			SET lider_id = idlider
				, suplente_id = idsuplente
				, com_des = descripcion
				, com_obs = observacion
				, com_ultimomodif = v_fecha_actual
				, creado_por_usuario = NULL
			WHERE min_id = idministerio;
			RAISE NOTICE 'Comite modificado';
		WHEN 'baja' THEN
			UPDATE membresia.comites
			SET com_obs = v_observacion,
				com_ultimomodif = v_fecha_actual,
				com_estado = FALSE,
				creado_por_usuario = NULL
			WHERE min_id = idministerio;
			RAISE NOTICE 'Comite dado de baja';
		WHEN 'reactivar' THEN
			UPDATE membresia.comites
			SET com_obs = '(REACTIVADO EN FECHA '||now()||')',
				com_ultimomodif = v_fecha_actual,
				com_estado = TRUE,
				creado_por_usuario = NULL
			WHERE min_id = idministerio;
			RAISE NOTICE 'Comite reactivado';
	END CASE;
	
END
$$;