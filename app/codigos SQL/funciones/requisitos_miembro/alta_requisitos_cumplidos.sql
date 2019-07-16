-- SP para alta de requisitos de miembros.
CREATE OR REPLACE FUNCTION membresia.alta_requisitos_cumplidos(idpersona integer, requisito varchar, obs text, idusuario integer)
RETURNS SETOF membresia.requisitos_cumplidos AS
$$
/**
*	Procedimiento: alta_requisitos_cumplidos
*	Parámetros: (idpersona integer, requisito varchar, obs text, idusuario integer)
*	Versión: 1.0
*	Fecha: 15/07/2019
*	Autor: Juan José González Ramírez
*	Email: juanftp100@gmail.com
*	Descripción: Registra el requisito del miembro según la palabra clave,
*	distinguiendo el nombre del documento registrado.
*/
DECLARE	
	temp_row membresia.requisitos_cumplidos;
	idrequisito integer;
	documento_registrado varchar;
	documento_ingresado varchar;
	idmiembro integer;
	documentos_obligatorios text[] := '{"BAUTISMO", "RECOMENDACION", "TESTIMONIO"}';
	item varchar;
	encontrado boolean;
	no_oblig boolean := false;
BEGIN

	-- Asignar variables.
	idmiembro := idpersona;
	documento_ingresado := TRIM(UPPER(requisito));
	----------------------									  
	temp_row.per_id = idpersona;	
	temp_row.fecha = now();
	temp_row.observacion = TRIM(UPPER(obs));
	temp_row.creado_por_usuario = idusuario;
	------------------------------------------
									  
	-- ##Verificar si el miembro tiene ese documento registrado.
	SELECT membresia.sp_averiguar_documento(idmiembro, documento_ingresado) INTO encontrado;		
	IF encontrado THEN
		-- Obtener el string del documento.
		SELECT descripcion FROM membresia.sp_get_documento(idmiembro, documento_ingresado) INTO documento_registrado;										  
		-- Verifica si el string coincide con alún registro de la tabla requisitos.
		SELECT req_id INTO idrequisito FROM referenciales.requisitos WHERE req_des = documento_registrado; 
		-- Asigna el iddocumento recuperado.
		temp_row.req_id = idrequisito;	
		IF FOUND THEN
		-- Si existe tal documento y coincide con los requisitos, es registrable.
			raise NOTICE 'SE ENCONTRO el DOCUMENTO %, insertando', documento_registrado;												  
			INSERT INTO membresia.requisitos_cumplidos VALUES (temp_row.*);
									  
			RETURN;									  
		END IF;
		-- ##Si el miembro no tiene registrado el documento.
	ELSIF referenciales.verificar_requisito(documento_ingresado) THEN	
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
				SELECT req_id INTO idrequisito FROM referenciales.requisitos WHERE req_des = documento_ingresado; 
				-- Asigna el iddocumento recuperado.
				temp_row.req_id = idrequisito;									  
				INSERT INTO membresia.requisitos_cumplidos VALUES (temp_row.*);
				RETURN;				
			END IF;
	END IF;				
END;
$$ LANGUAGE plpgsql;
									  
									  
-- Pruebas
--SELECT membresia.alta_requisitos_cumplidos(2, 'DISCIPULADO', 'NINGUNA', null);									  