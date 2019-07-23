CREATE OR REPLACE FUNCTION referenciales.get_personas_activas_json()
RETURNS json AS
$$
	SELECT 
		ARRAY_TO_JSON(
               ARRAY_AGG(
                    ROW_TO_JSON(
                        data
                    ) 
                )
            )
     FROM 
           (
            SELECT * FROM referenciales.get_personas_activas()
            ) data;

$$ LANGUAGE sql;
SELECT referenciales.get_personas_activas_json();