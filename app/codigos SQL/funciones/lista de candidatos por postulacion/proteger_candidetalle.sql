CREATE OR REPLACE FUNCTION membresia.proteger_candidetalle()
RETURNS TRIGGER AS 
$$
/**
 * Función tipo trigger proteger_candidetalle.
 * Protege a la tabla de realizar inserciones o actualizaciones sobre
 * registros anulados.
 * Autor: Juan José González Ramírez 
 */
BEGIN
	
	IF TG_OP = 'INSERT' THEN
	
		PERFORM membresia.verifica_estado_postulacion(NEW.post_id);
		IF NOT FOUND THEN
			RAISE EXCEPTION 'Esta postulación no es válida, no se reciben nuevos datos' USING ERRCODE = '10001';
		ELSE
			RETURN NEW;
		END IF;
	
	ELSEIF TG_OP = 'UPDATE' THEN
	
		PERFORM membresia.verifica_estado_postulacion(NEW.post_id);
		IF NOT FOUND THEN
			RAISE EXCEPTION 'Esta postulación no es válida, no se actualizan nuevos datos' USING ERRCODE = '10001';
		ELSE
			RETURN NEW;
		END IF;
	
	END IF;
	
END
$$ LANGUAGE plpgsql;

CREATE TRIGGER t_candidetalle BEFORE INSERT OR UPDATE ON membresia.candi_detalle
FOR EACH ROW EXECUTE PROCEDURE membresia.proteger_candidetalle();
