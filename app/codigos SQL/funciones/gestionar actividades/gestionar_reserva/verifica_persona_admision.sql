create or replace function actividades.verifica_persona_admision(id integer)
returns boolean as 
$$
begin
	perform * from membresia.admision_persona ap where adp_estado is true and adp_id = id;
	if found then
		return true;
	else
		raise exception 'Esta persona no tiene formulario de admision o esta desactivado';
		return false;
	end if;
end
$$ language plpgsql;