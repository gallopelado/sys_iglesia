create or replace function sp_buscarpersona(palabra varchar)
returns boolean as
$$
begin
	
	perform per_id, per_nombres || ' ' || per_apellidos as persona from referenciales.personas
	where to_tsvector(per_nombres || ' ' || per_apellidos ) @@ to_tsquery((select plainto_tsquery(palabra)::text));
	if found then
		return true;
	else
		return false;
	end if;
	
end
$$
language plpgsql;
