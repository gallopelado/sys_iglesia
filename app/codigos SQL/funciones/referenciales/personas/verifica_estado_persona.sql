CREATE OR REPLACE FUNCTION referenciales.verifica_estado_persona(integer)
RETURNS boolean AS 
$$
BEGIN
	
		PERFORM per_id FROM referenciales.personas 
		WHERE per_id = $1 AND per_fechabaja IS NULL AND per_razonbaja IS NULL;
		IF FOUND THEN
			RETURN TRUE;
		ELSE
			RAISE NOTICE 'Esta persona ha sido desactivada o dada de baja o no existe en la BD.';
			RETURN FALSE;
		END IF;
	
END
$$ LANGUAGE plpgsql;

