CREATE OR REPLACE FUNCTION cursos.registrar_desercion(mallaid integer, curid integer, perid integer
	, mdid integer, alddescripcion text, aldestado boolean, creacionfecha timestamp, creacionusuario integer)
RETURNS BOOLEAN AS 
$$
/**
 * Procedimiento: registrar_desercion
 * Autor: Juan José González Ramírez
 * Fecha creación: 2020-09-13
 * Parametros: 
 * Descripción: Procedimiento que realizará el registro de la deserción del alumno
 * 
 */
BEGIN
	
	--Insertar desercion
	INSERT INTO cursos.alumno_desercion
	(malla_id, cur_id, per_id, md_id, ald_descripcion, ald_estado, modificacion_fecha, modificacion_usuario)
	VALUES(mallaid, curid, perid, mdid, TRIM(alddescripcion), true, now(), creacionusuario);

	--Actualizar estado de la inscripción
	UPDATE cursos.inscripcion_curso
	SET estado=false, modificacion_fecha=now(), modificacion_usuario=creacionusuario
	WHERE malla_id=mallaid AND cur_id=curid AND per_id=perid;

	RETURN true;

END
$$ LANGUAGE PLPGSQL;

SELECT cursos.registrar_desercion(2, 1, 6, 1, 'nunca justificó ausencias', true, null, null);
SELECT * FROM cursos.alumno_desercion;
SELECT * FROM cursos.inscripcion_curso;