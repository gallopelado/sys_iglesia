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
