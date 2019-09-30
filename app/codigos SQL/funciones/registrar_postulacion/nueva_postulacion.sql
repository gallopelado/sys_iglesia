CREATE OR REPLACE FUNCTION membresia.nueva_postulacion(
	minid integer
	, postdes TEXT
	, postdoc TEXT
	, postestado boolean
	, postiniciopostu date
	, postfinpostu date	
	, creadoporusuario integer
	, detalle_idprofesion TEXT
	, detalle_cantidad TEXT
)
RETURNS TEXT AS
$$
/**
 * Funcion: nueva_postulacion.
 * Descripción: Da de alta un nuevo registro de postulación.
 * Parámetros: postdes text, postdoc text, postestado boolean, postiniciopostu date, postfinpostu date, creadoporusuario integer
 * Autor: Juan José González Ramírez <juanftp100@gmail.com>	
 * Version: 1.1
 * Fecha: 26-09-2019
 */
DECLARE	

	--ID del la tabla.
	v_idpostulacion integer;
	-- Obtiene el último valor mas uno.
	v_autoidpostulacion integer := (SELECT COALESCE(max(post_id), 0) + 1 FROM membresia.cabe_postulacion);

	-- Variables para el FOR
	v_idprofesion integer;
	v_cantidad integer;

	-- El resto de variables.
	v_minid integer := minid; 
	v_postdes TEXT := TRIM(UPPER(postdes));
	v_postdoc TEXT := postdoc;
	v_postestado boolean := postestado;
	v_postiniciopostu date := postiniciopostu;
	v_postfinpostu date	:= postfinpostu;

	-- Usuario y fecha de creacion.
	v_creadoporusuario integer := null;	
	v_fechacreacion timestamp := now();

	-- Arrays para los detalles.
	array_idprofesion TEXT[] := string_to_array( detalle_idprofesion, ',' );
	array_cantidad TEXT[] := string_to_array( detalle_cantidad, ',' );

	-- Datos de cantidad de elementos del los arrays.
	v_cont_idprofesion integer := array_upper( array_idprofesion, 1 );
	v_cont_cantidad integer := array_upper( array_cantidad, 1 );

BEGIN
	
	-- Controlar el detalle, deben coincidir.
	IF v_cont_idprofesion != v_cont_cantidad THEN
		RAISE EXCEPTION 'Las cantidades de idprofesion y cantidad no coinciden !!!';		
	END IF;

	-- Si existe el nombre de imagen.
	IF v_postdoc IS NOT NULL THEN
		v_postdoc := v_autoidpostulacion::varchar ||'_'|| postdoc;
	END IF;
	
	-- Insertar cabecera.
	INSERT INTO membresia.cabe_postulacion
	(post_id, min_id, post_des, post_doc, post_estado, post_iniciopostu, post_finpostu, post_fechaprocesado, creado_por_usuario, post_fechacreacion)
	VALUES
	(
		v_autoidpostulacion
		, v_minid
		, v_postdes
		, v_postdoc
		, v_postestado
		, v_postiniciopostu
		, v_postfinpostu
		, NULL
		, v_creadoporusuario --usuario
		, v_fechacreacion
	) RETURNING post_id INTO v_idpostulacion;

	-- Procesar el detalle.		
	FOR i IN 1..v_cont_idprofesion
	LOOP
		
		-- Se recuperan los valores de los array de a uno.
		v_idprofesion := array_idprofesion[i]::INT;
		v_cantidad := array_cantidad[i]::INT;
	
		-- Insertar.
		INSERT INTO membresia.postu_detalle
		(post_id, pro_id, cantidad)
		VALUES(v_idpostulacion, v_idprofesion, v_cantidad);
		
	END LOOP;
	
	-- Retorna nombre del documento.
	RETURN v_postdoc;
	
END
$$ LANGUAGE plpgsql;