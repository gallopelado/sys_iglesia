--SELECT req_id, req_des FROM referenciales.requisitos;
-- Retorna todos los registros de requisitos.
CREATE OR REPLACE FUNCTION referenciales.obtener_todos_requisitos()
RETURNS SETOF referenciales.td_referencial AS
$$
BEGIN
	
	RETURN QUERY
	SELECT * FROM referenciales.requisitos;
	RETURN;
END;
$$ LANGUAGE plpgsql;
--DROP FUNCTION referenciales.obtener_datos_refsimple();
--CREATE TYPE referenciales.td_referencial AS (id integer, descripcion varchar);
SELECT referenciales.obtener_todos_requisitos();
