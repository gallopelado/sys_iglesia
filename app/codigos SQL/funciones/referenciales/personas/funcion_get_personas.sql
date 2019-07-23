/* Descripcion: Función que retorna id, nombres y apellidos de la tabla personas.
 * Autor: Juan José González Ramírez
 * Email: juanftp100@gmail.com
 * Versión: 1.0
 * Fecha: 21/07/2019
*/
-- Creat TYPE
--CREATE TYPE referenciales.td_persona_simple AS ( idpersona integer, persona text );
CREATE OR REPLACE FUNCTION referenciales.get_personas()
RETURNS SETOF referenciales.td_persona_simple AS
$$

	SELECT 
		per_id idpersona,
		per_nombres||' '||per_apellidos persona
	FROM 
		referenciales.personas;

$$ LANGUAGE sql;

--SELECT * FROM referenciales.get_personas();