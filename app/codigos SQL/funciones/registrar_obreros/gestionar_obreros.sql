CREATE OR REPLACE PROCEDURE membresia.gestionar_obreros(
	opcion varchar, idcomite integer, idpersona integer
	, entrena boolean, obs TEXT, idusuario integer
) LANGUAGE plpgsql AS $$
/*
 * Procedimiento gestionar obreros
 * Se define según las operaciones
 * registrar, modificar, baja, reincorporar
 * de los obreros para los comités.
 * Autor: Juan José González Ramírez <juanftp100@gmail.com>
 * Versión: 0.1
 * 
 */
DECLARE
	v_obs TEXT := TRIM(upper(obs));
	v_actual := now();
BEGIN
	-- Casos
	CASE opcion
		WHEN 'registrar' THEN
			-- Verificar si esta en candi_admitidos.
		WHEN 'modificar' THEN
		WHEN 'baja' THEN
		WHEN 'reincorporar' THEN
		ELSE
			RAISE EXCEPTION 'Ninguna opción es correcta.' USING ERRCODE='20099';
	END CASE;
END
$$;