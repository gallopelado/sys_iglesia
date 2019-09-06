CREATE OR REPLACE FUNCTION membresia.proteger_cabepostulacion()
RETURNS TRIGGER AS
$$

/**
 * Funcion: proteger_cabepostulacion
 * Tipo: Trigger
 * Descripción: 
 * En base a validaciones de fecha permitir insert
 * Autor: Juan José González Ramírez <juanftp100@gmail.com>
 * 
 */
DECLARE
	-- Tabla temporal
	temp_row membresia.cabe_postulacion;
	v_fecha_valida boolean;
BEGIN
	
	-- Asignacion de valores.
	temp_row.post_des = NEW.post_des;
	temp_row.post_doc = NEW.post_doc;
	temp_row.post_estado = NEW.post_estado;
	temp_row.post_iniciopostu = NEW.post_iniciopostu;
	temp_row.post_finpostu = NEW.post_finpostu;
	temp_row.post_fechaprocesado = NEW.post_fechaprocesado;
	temp_row.creado_por_usuario = NEW.creado_por_usuario;
	temp_row.post_fechacreacion = NEW.post_fechacreacion;

	-- Validar fechainicio y fecha fin
	v_fecha_valida := membresia.verifica_fechas_postulacion( temp_row.post_iniciopostu, temp_row.post_finpostu );
	
	IF v_fecha_valida = TRUE THEN
		
		-- Insertar.
		INSERT INTO membresia.cabe_postulacion VALUES (temp_row.*);			
	
		RETURN NEW;
	
	END IF;
	
	RETURN NULL;
END

$$ LANGUAGE plpgsql;

-- el TRIGGER
CREATE TRIGGER t_insert_cabe_postulacion
BEFORE INSERT ON membresia.cabe_postulacion FOR EACH ROW
EXECUTE PROCEDURE membresia.proteger_cabepostulacion();


INSERT INTO membresia.cabe_postulacion
(post_des, post_doc, post_estado, post_iniciopostu, post_finpostu, post_fechaprocesado, creado_por_usuario, post_fechacreacion)
VALUES('vacantes guitarra', '/documentos', true, '2019-01-01', '2019-01-01', null, null, now());


