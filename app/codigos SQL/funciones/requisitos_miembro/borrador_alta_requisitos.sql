-- SP para alta y modificacion de requisitos de miembros
CREATE OR REPLACE FUNCTION membresia.alta_requisitos_cumplidos(idpersona integer, idrequisito integer, obs text, idusuario integer)
RETURNS SETOF membresia.requisitos_cumplidos AS
$$
DECLARE	
	temp_row membresia.requisitos_cumplidos;
	documento_registrado varchar;
BEGIN
	DO $$
	DECLARE
		documento_registrado varchar;
		documento_ingresado varchar := 'EVANGELISMO';
		idmiembro integer := 2;
		documentos_obligatorios text[] := '{"BAUTISMO", "RECOMENDACION", "TESTIMONIO"}';
		item varchar;
		encontrado boolean;
		no_oblig boolean := false;
	BEGIN
		-- ##Verificar si el miembro tiene ese documento registrado.
		SELECT membresia.sp_averiguar_documento(idmiembro, documento_ingresado) INTO encontrado;		
		IF encontrado THEN
			-- Obtener el string del documento.
			SELECT membresia.sp_get_documento(idmiembro, documento_ingresado) INTO documento_registrado;
			-- Verifica si el string coincide con alún registro de la tabla requisitos.
			PERFORM req_id, req_des FROM referenciales.requisitos WHERE req_des = documento_registrado; 
			IF FOUND THEN
				-- Si existe tal documento y coincide con los requisitos, es registrable.
				raise NOTICE 'SE ENCONTRO el DOCUMENTO %, insertando', documento_registrado;
				--INSERT INTO membresia.requisitos_cumplidos(per_id, req_id, fecha, observacion, creado_por_usuario)
				--VALUES ();		
			END IF;
		-- ##Si el miembro no tiene registrado el documento.
		ELSE
			RAISE WARNING 'Lo siento, el documento no existe.';
			-- Recorrer array para detectar si existe coincidencia de nombres con los
			-- registros obligatorios.
			FOREACH item IN ARRAY documentos_obligatorios LOOP
				--RAISE NOTICE '%', i;
				-- Si coicide el string con alguno, para el loop.
				IF documento_ingresado = item THEN					
					RAISE EXCEPTION 'Elemento encontrado %', item;
					no_oblig := true;
					RETURN;
				END IF;
			END LOOP;
			-- En caso de FALSE, significa que el string no es un documento obligatorio.
			IF NOT no_oblig THEN
				-- Insertar
				RAISE NOTICE 'Guardando documento %', documento_ingresado;
			END IF;
		END IF;			
	END;
	$$ LANGUAGE plpgsql;
	
	
END;
$$ LANGUAGE plpgsql;
