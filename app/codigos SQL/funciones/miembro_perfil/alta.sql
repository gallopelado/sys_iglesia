CREATE OR REPLACE FUNCTION 
	membresia.alta_miembroperfil(idmiembro integer, serviren varchar, 
	cualipers varchar, actiminis varchar, anteced varchar, 
	estado boolean, creadoporusuario integer)
RETURNS BOOLEAN AS
/**
*	Procedimiento: alta_miembroperfil
*	Descripción: registrar, actualizar datos de perfil
*	de los miembros.
*	Versión: 1.0
*	Autor: Juan José González Ramírez
*	Email: juanftp100@gmail.com
*/
$$
DECLARE
	--Variables
	v_id INTEGER := idmiembro;
	v_serviren VARCHAR := TRIM(UPPER(serviren));
	v_cualipers VARCHAR := TRIM(UPPER(cualipers));
	v_actiminis VARCHAR := TRIM(UPPER(actiminis));
	v_anteced VARCHAR := TRIM(UPPER(anteced));
	v_fecha TIMESTAMP := now();
	v_estado BOOLEAN := estado;
	v_iduser INTEGER := creadoporusuario;

BEGIN

	-- Verificar si ya esta registrado en miembro_perfil.
	PERFORM 
		mper_id 
	FROM 
		membresia.miembro_perfil 
	WHERE
		mper_id = v_id;
	IF not found THEN
		-- Realizar inserción.
		INSERT INTO
			membresia.miembro_perfil(mper_id, mper_serviren, 
			mper_cualipers, mper_actiminis, mper_anteced, 
			mper_fecha, mper_estado, creado_por_usuario)
		VALUES
			(
				v_id,
				v_serviren,
				v_cualipers,
				v_actiminis,
				v_anteced,
				v_fecha,
				v_estado,
				v_iduser
			);
		RAISE INFO 'SE REGISTRO CORRECTAMENTE';
		RETURN TRUE;
	ELSE
		-- Realizar actualización.
		UPDATE 
			membresia.miembro_perfil
		SET
			mper_serviren = v_serviren,
			mper_cualipers = v_cualipers,
			mper_actiminis = v_actiminis,
			mper_anteced = v_anteced,
			mper_fecha = v_fecha,
			mper_estado = v_estado,
			creado_por_usuario = v_iduser
		WHERE
			mper_id = v_id;
		RAISE INFO 'SE MODIFICO CORRECTAMENTE';			
		RETURN TRUE;
	END IF;
END;
$$ LANGUAGE plpgsql;