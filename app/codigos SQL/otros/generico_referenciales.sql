create or replace function getall_referencial(varchar)
returns table(id integer, descripcion varchar) as
/**
 * Procedimiento getall_referencial
 * Descripción: Obtiene id y descripcion de las
 * tablas simples. 
 * Version: 1.0
 * Autor: Juan José González Ramírez
 * Email: juanftp100@gmail.com
 */
$$
begin
	return query execute 'select * from '||$1||';';
	return;
end;
$$ language plpgsql;

select getall_referencial('referenciales.sangre');



-- Para generar json
CREATE OR REPLACE FUNCTION get_referencial_json(tabla varchar)
RETURNS json AS
$$
/**
* Funcion: get_referencial_json
* Parametros: tabla varchar
* Descripcion: De cualquier tabla simple(id, descripcion)
* genera un json de sus registros.
* Autor: Juan José González Ramírez <juanftp100@gmail.com>
* Version: 1.0
* Fecha: 10-09-2019
*/

	 SELECT 
		array_to_json(
			array_agg(
				data
			)
		) resultado
	FROM (
	
		SELECT * FROM public.getall_referencial(tabla)
	
	) data;

$$ LANGUAGE sql;
