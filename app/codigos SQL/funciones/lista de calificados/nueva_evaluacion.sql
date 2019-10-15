CREATE OR REPLACE FUNCTION membresia.nueva_evaluacion(idpostulacion integer, postulantes TEXT)
RETURNS boolean AS
$$
/**
 * Función: nueva_evaluacion
 * Inserta los candidatos calificados según postulación.
 * Autor: Juan José González Ramírez
 */
DECLARE
	v_idcandidato integer;
	array_postulante TEXT[];
	size_postulante integer;
	v_postulantes TEXT;
	nro_vacantes bigint := (SELECT SUM(cantidad) FROM membresia.postu_detalle WHERE post_id = idpostulacion);

BEGIN
	
	v_postulantes := trim(postulantes);
	
	IF v_postulantes IS NULL OR v_postulantes = '' THEN
		RAISE EXCEPTION 'No se ha recibido ningún postulante' USING ERRCODE = '20098';
		RETURN  FALSE;
	END IF;
	
	-- Cargar array.
	array_postulante := string_to_array(v_postulantes, ',');
	
	-- Obtener el tamaño.
	size_postulante := array_upper(array_postulante, 1);
	IF nro_vacantes < size_postulante THEN
		RAISE EXCEPTION 'Ha superado el límite de cupos disponibles' USING ERRCODE = '20099';
		RETURN  FALSE;
	END IF;

	--Actualizar fecha de calificado.
	UPDATE membresia.cabe_postulacion SET post_fechacalificado = now()
	WHERE post_id = idpostulacion;

	-- Ahora cargar los calificados
	FOR i IN 1..size_postulante
	LOOP
	
		v_idcandidato := array_postulante[i]::int;
	
		INSERT INTO membresia.candi_admitidos(post_id, mo_id)
		VALUES (idpostulacion, v_idcandidato);
	
	END LOOP;

	RAISE NOTICE 'Se ha calificado exitosamente';
	RETURN TRUE;
	
END
$$ LANGUAGE plpgsql;

--SELECT membresia.nueva_evaluacion(4, '8,2,3');
