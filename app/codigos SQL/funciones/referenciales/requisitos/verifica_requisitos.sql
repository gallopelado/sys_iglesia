-- Verifica si existe el requisito según palabra clave.
-- Retorna un booleano.
CREATE OR REPLACE FUNCTION referenciales.verificar_requisito(varchar) 
RETURNS boolean AS
$$
BEGIN

	PERFORM req_des FROM referenciales.requisitos WHERE req_des = $1;
	IF found THEN	
		RETURN true;
	END IF;
	
	RAISE EXCEPTION 'Lamentablemente no encontramos este requisito.' USING ERRCODE = '10500';
	RETURN false;

END;
$$ LANGUAGE plpgsql;

--SELECT referenciales.verificar_documento('b');