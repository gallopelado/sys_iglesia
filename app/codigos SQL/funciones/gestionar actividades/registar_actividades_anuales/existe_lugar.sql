create or replace function referenciales.existe_lugar(text)
returns boolean as 
$$
/*
 * Funcion existe_lugar
 * Parametros: text
 * Retorna boolean
 * Verifica si la cadena ingresada existe en la tabla
 * lugares.
 * version: 1.0
 * Autor: Juan José González Ramírez <juanftp100@gmail.com>
*/
declare
	v_lugar text := trim($1);
begin
	perform * from referenciales.lugares where lug_des = v_lugar;
	if found then
		return true;
	end if;
	raise exception 'No existe este lugar' using ERRCODE = '30001';
	return false;
end
$$ language plpgsql;

--select referenciales.existe_lugar('pepe');