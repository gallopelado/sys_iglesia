-- Retorna en formato json el resultado de la función membresia.cantidaddocumentos_miembro()

CREATE OR REPLACE FUNCTION membresia.sp_cantidaddocumentos_miembro_json() 
RETURNS json AS
$$
DECLARE
	arrayObjeto json;	
BEGIN

	SELECT 
		ARRAY_TO_JSON(
			ARRAY_AGG(
				ROW_TO_JSON(
					data
				)
			)
		) INTO arrayObjeto
	FROM 
	(
		SELECT membresia.cantidaddocumentos_miembro()

	) as data;

	RETURN arrayObjeto;	
	
END;
$$ LANGUAGE plpgsql;
--SELECT membresia.sp_cantidaddocumentos_miembro_json();