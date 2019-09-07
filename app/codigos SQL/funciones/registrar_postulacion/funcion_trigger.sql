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
	v_fecha_valida boolean;
	v_segunda_posibilidad boolean;
BEGIN
	
	IF TG_OP = 'INSERT' THEN
		-- Validar fechainicio y fecha fin
		v_fecha_valida := membresia.verifica_fechas_postulacion( NEW.post_iniciopostu, NEW.post_finpostu );
	
		IF v_fecha_valida IS TRUE THEN			
		
			-- Devuelve la estructura grabada NEW.
			RETURN NEW;
		
		END IF;
	ELSIF TG_OP = 'UPDATE' THEN
		
		v_fecha_valida := membresia.verifica_fechas_postulacion( OLD.post_iniciopostu, NEW.post_finpostu );
		v_segunda_posibilidad := membresia.verifica_fechas_postulacion( NEW.post_iniciopostu, NEW.post_finpostu );
		
		IF (v_fecha_valida IS TRUE) OR (v_segunda_posibilidad IS TRUE) THEN			
		
			-- Devuelve la estructura grabada NEW.
			RETURN NEW;
		
		END IF;
	END IF;

	RETURN NULL;

END; -- Fin del procedimiento.

$$ LANGUAGE plpgsql;
-- el disparador.
CREATE TRIGGER t_insert_cabe_postulacion
BEFORE INSERT OR UPDATE ON membresia.cabe_postulacion FOR EACH ROW
EXECUTE PROCEDURE membresia.proteger_cabepostulacion();


INSERT INTO membresia.cabe_postulacion
(post_id,post_des, post_doc, post_estado, post_iniciopostu, post_finpostu, post_fechaprocesado, creado_por_usuario, post_fechacreacion)
VALUES(
(SELECT COALESCE(max(post_id),0)+1 FROM membresia.cabe_postulacion), 
'vacantes musica', '/documentos', true, '2019-09-07', '2019-10-01', null, null, now());



