CREATE OR REPLACE FUNCTION membresia.persona_requisitos(idpersona integer, idrequisitos varchar, observaciones varchar, idusuario integer)
RETURNS boolean AS
$$
DECLARE
	array_idrequisito text[];
	array_observaciones text[];
	v_idpersona integer;
	v_idrequisitos varchar;	
	v_observaciones varchar;
	v_idusuario integer;
	v_cantidad_id integer;
	
	-- Variables para el FOR
	v_idrequisito integer;
	v_observacion varchar;

BEGIN
	
	-- Asignar variables.
	v_idpersona := idpersona;
	v_idrequisitos := idrequisitos;
	v_observaciones := observaciones;
	v_idusuario := null;

	-- Procesar variables.
	array_idrequisito := string_to_array( v_idrequisitos, ',' );
	array_observaciones := string_to_array( v_observaciones, ',' );
	v_cantidad_id := array_upper( array_idrequisito, 1 );

	-- Mostrar.
	RAISE INFO 'Los idrequisitos ingresados son %', array_idrequisito;
	RAISE INFO 'Las observaciones ingresadas son %', array_observaciones;
	RAISE INFO 'Cantidad de id en el array iderequisito %', v_cantidad_id;

	-- Recorrer.
	FOR i IN 1..v_cantidad_id
	LOOP		
		v_idrequisito := array_idrequisito[i]::INT;
		v_observacion := array_observaciones[i];
		RAISE INFO '-------------------------------';
		RAISE INFO '-- EN EL LOOP ---';
		RAISE INFO 'IDREQUISITO = %', v_idrequisito;
		RAISE INFO 'OBSERVACION = %', v_observacion;
		RAISE INFO '-------------------------------';
	
		--INSERTAR
		INSERT INTO membresia.requisitos_cumplidos(per_id, req_id, fecha, observacion, creado_por_usuario)
		VALUES (v_idpersona, v_idrequisito, now(), v_observacion, null);
		
	END LOOP;
	
	RETURN true;
	
END;
$$ LANGUAGE plpgsql;
--SELECT membresia.persona_requisitos(2, '5,4', 'OBS1,OBS2', 0);
--DROP FUNCTION membresia.persona_requisitos(idpersona integer, requisitos varchar, observaciones varchar, idusuario integer);

	