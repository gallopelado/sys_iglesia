-- Retorna todos los registros de requisitos en formato json.
CREATE OR REPLACE FUNCTION referenciales.obtener_todos_requisitos_json()
RETURNS json AS
$$
DECLARE
	arrayjson json;
BEGIN
	
	SELECT
		ARRAY_TO_JSON(
			ARRAY_AGG(
				ROW_TO_JSON(
					data
				)
			)
		) INTO arrayjson
	FROM 
		(
			SELECT referenciales.obtener_todos_requisitos()
		) data;
	
	RETURN arrayjson;
	
END;
$$ LANGUAGE plpgsql;
SELECT referenciales.obtener_todos_requisitos_json()