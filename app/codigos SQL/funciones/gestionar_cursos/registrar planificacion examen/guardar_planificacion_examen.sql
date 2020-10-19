-----------------------------------------------------------------------------
--
-- Crear una funcion que guarde los datos del formulario de planificación de examenes.
--
-----------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION cursos.guardar_planificacion_examen(mallaid INTEGER, asiid INTEGER, numid INTEGER, perid INTEGER
, exaid INTEGER, vfechainicio DATE, vhora TIME, vturno turno, curid INTEGER, creacionusuario INTEGER)
RETURNS BOOLEAN AS
$$
/**
 * Función: guardar_planificacion_examen
 * Inserta fecha y examen en los rangos planificados.
 * Autor: Juan José González Ramírez
 */
DECLARE
	reg_contados INTEGER;
BEGIN
	PERFORM malla_id FROM cursos.detalle_planificacion
	where malla_id = mallaid and asi_id = asiid and num_id = numid and turno = vturno and per_id = perid and
	vfechainicio between fechainicio and fechafin;
	IF FOUND THEN
		--Antes de insertar, verificar si ya existe el mismo con estado True
		SELECT COUNT(*) INTO reg_contados FROM cursos.planificacion_examen 
		WHERE malla_id=mallaid AND cur_id=curid AND asi_id=asiid AND num_id=numid AND turno=vturno AND per_id=perid
		AND exa_id=exaid AND planex_estado IS TRUE;
		IF reg_contados > 0 THEN
			RAISE EXCEPTION 'Ya existe este examen, debe anular para volver a registrar el mismo';
			RETURN FALSE;
		END IF;
		--Hacer insercion
		INSERT INTO cursos.planificacion_examen
		(malla_id, cur_id, asi_id, num_id, turno, per_id, exa_id, planex_fecha, planex_hora
		 , planex_estado, creacion_fecha, creacion_usuario)
		VALUES(mallaid, curid, asiid, numid, vturno, perid, exaid, vfechainicio, vhora
			   , true, now(), creacionusuario);

		RETURN TRUE;
	END IF;
	RAISE EXCEPTION 'No es posible planificar fuera de fecha de planificacion!';
	RETURN FALSE;
END;
$$ LANGUAGE PLPGSQL;