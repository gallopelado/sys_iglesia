CREATE OR REPLACE PROCEDURE membresia.nueva_lista_candidatos(idpostulacion integer, id_miembros text)
LANGUAGE plpgsql AS
$$

/**
* Procedimiento: nueva_lista_candidatos
* Parametros: idpostulacion integer, id_miembros text
* Descripcion: registra la lista de candidatos a una postulación activa.
* Autor: Juan José González Ramírez <juanftp100@gmail.com>
* Version: 1.0
* Fecha: 07-10-2019
*/

DECLARE
	id_miembro integer;
	
	arrayid_miembros TEXT[];

	--Limpiar de espacios.
	v_idmiembros TEXT := TRIM(id_miembros);
	
	longitud_array integer; 

BEGIN
	
	-- Verificar si no esta null o vacía la cadena de id_miembros.
	IF id_miembros IS NULL OR id_miembros = '' THEN
		RAISE EXCEPTION 'id_miembros esta vacía!!' USING ERRCODE = '20001';
	END IF;

	-- Cargar
	-- Convertir cadena en array.
	arrayid_miembros := string_to_array(v_idmiembros, ',');

	-- Contar los elementos del array.
	longitud_array := array_upper(arrayid_miembros, 1);

	FOR i IN 1..longitud_array 
	LOOP
	
		id_miembro := arrayid_miembros[i]::int;
	
		INSERT INTO membresia.candi_detalle(post_id, mo_id) VALUES (idpostulacion, id_miembro);
	
	END LOOP;
	

	-- Excepciones
	EXCEPTION
	WHEN foreign_key_violation THEN
		RAISE EXCEPTION 'Estas queriendo registrar con datos inexistente, estas reventando la FK, pendejo. CODIGO: % %', SQLERRM,SQLSTATE;
	
END
$$;