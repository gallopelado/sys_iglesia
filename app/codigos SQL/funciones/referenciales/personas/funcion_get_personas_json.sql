/* Descripcion: Función que retorna un array de objetos json.
 * Autor: Juan José González Ramírez
 * Email: juanftp100@gmail.com
 * Versión: 1.0
 * Fecha: 21/07/2019
*/
CREATE OR REPLACE FUNCTION referenciales.get_personas_json()
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
			SELECT * FROM referenciales.get_personas()
		) data;

$$ LANGUAGE sql;

--SELECT * FROM referenciales.get_personas_json();