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

--Construyendo el INSERT
-- Quiero todos los nombres de las columnas de algun referencial
create or replace function insertone_referencial(esquema varchar, tabla varchar, valor text)
returns boolean as
/**
 * Procedimiento insertone_referencial
 * Descripción: Inserta un registro en 
 * tablas simples. 
 * Version: 1.0
 * Autor: Juan José González Ramírez
 * Email: juanftp100@gmail.com
 */
$$
declare
	v_esquema varchar := esquema;
	v_tabla varchar := tabla;
	v_valor text := UPPER(TRIM(valor));
	v_columna varchar;
begin
	
	if (v_esquema is null OR esquema = '') OR (v_tabla is null OR v_tabla = '') OR (v_valor is null OR v_valor = '') then
		raise exception 'Alguno de los argumentos esta vacio o nulo! esquema=%, tabla=%, valor=%', v_esquema, v_tabla, v_valor;
		return false;
	end if;
	
	select columna 
	into v_columna 
	from (
		select 
			column_name columna, 
			(row_number() OVER ()) as rnum 
		from 
			information_schema.columns 
		where 
			table_name = tabla and table_schema = esquema
	) x where rnum = 2;	
	raise notice 'Alguno de los argumentos! esquema=%, tabla=%, valor=%', v_esquema, v_tabla, v_valor;
	execute 'insert into '||esquema||'.'||tabla||'('||v_columna||') values (UPPER('||''''||valor||''''||'));';
	if found then
		return true;
	end if;
	exception when null_value_not_allowed then
		raise exception 'Hubo problemas esquema=%, tabla=%, v_columna=%, valor=%',esquema,tabla,v_columna,valor using ERRCODE='16000';
		return false;
end;
$$ language plpgsql;

select public.insertone_referencial('referenciales', 'ciudades', 'encarnación');
select public.getall_referencial('referenciales.ciudades');

