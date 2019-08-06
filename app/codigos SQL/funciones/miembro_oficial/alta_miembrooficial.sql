CREATE OR REPLACE FUNCTION 
membresia.alta_miembrooficial(
	id integer,
	fechaconversion date,
	fechabautismo date,
	lugarbautismo varchar,
	oficiador varchar,
	fechainiciomembresia date,
	razonaltaid integer,
	estadomembresia membresia.estado_membresia,
	bautizadoeniglesia boolean,
	padresmiembros boolean,
	recibioes boolean,
	obs text,
	creadoporusuario integer
) 
RETURNS boolean AS
$$
/**
 * Procedimiento: alta_miembrooficial
 * Esquema: membresia
 * Versión: 1.0
 * Fecha: 04/08/2019
 * @author: Juan José González Ramírez
 * @email: juanftp100@gmail.com
 */
DECLARE
	temp_row membresia.miembros_oficiales;
	requisito boolean;
BEGIN
	-- Asignación y limpieza.
	temp_row.mo_id = id;
	temp_row.mo_fechaconversion := fechaconversion;
	temp_row.mo_fechabautismo := fechabautismo;
	temp_row.mo_lugarbautismo := TRIM(UPPER(lugarbautismo));
	temp_row.mo_oficiador := TRIM(UPPER(oficiador));
	temp_row.mo_fechainiciomembresia := fechainiciomembresia;
	temp_row.razonalta_id := razonaltaid;
	temp_row.mo_estadomembresia := estadomembresia;
	temp_row.mo_bautizadoeniglesia := bautizadoeniglesia;
	temp_row.mo_padresmiembros := padresmiembros;
	temp_row.mo_recibioes := recibioes;
	temp_row.mo_obs := TRIM(UPPER(obs));
	temp_row.creado_por_usuario := creadoporusuario;
	
	-- Verificación de requisitos cumplidos.
	SELECT membresia.controlar_requisitos(temp_row.mo_id, temp_row.razonalta_id) INTO requisito;
	IF requisito THEN
		-- Insertar.
		INSERT INTO 
			membresia.miembros_oficiales(mo_id, mo_fechaconversion, mo_fechabautismo, 
			mo_lugarbautismo, mo_oficiador, mo_fechainiciomembresia, razonalta_id, 
			mo_estadomembresia, mo_bautizadoeniglesia, mo_padresmiembros, mo_recibioes, 
			mo_obs, creado_por_usuario)
		VALUES
			(temp_row.*);
		RETURN TRUE;
	ELSE
		--No se encontró.
		RAISE EXCEPTION 'Esta persona no tiene los requisitos para ser miembro' USING ERRCODE = '15003';
		RETURN FALSE;
	END IF;

	
END;
$$ LANGUAGE plpgsql;

