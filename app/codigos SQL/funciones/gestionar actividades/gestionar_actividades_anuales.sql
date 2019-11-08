create or replace procedure membresia.gestionar_actividades_anuales(
	opcion varchar, anhohabil integer, eveid integer, lugid integer, actfecha date, 
	acthora time, plazid integer, actrepite boolean, actobs text, minid integer, creadoporusuario integer
) language plpgsql as $$
/**
 * Procedimiento gestionar_actividades_anuales
 * Se define el CRUD para las actividades anuales
 * con opciones como:
 * registrar, modificar, eliminar, repetir_por_año
 * Autor: Juan José González Ramírez <juanftp100@gmail.com>
 * versión 1.0
*/
begin
	CASE opcion
		WHEN 'registrar' THEN
		WHEN 'modificar' THEN
		WHEN 'eliminar' THEN
		WHEN 'repetir_por_año' THEN
	END CASE;
end
$$;