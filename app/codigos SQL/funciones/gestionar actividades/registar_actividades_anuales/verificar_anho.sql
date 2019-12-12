create or replace function actividades.verificar_anho(integer) returns boolean as $$
begin
	--Cuando el anho es activo y no adelantado.
	perform anho_id from referenciales.anho_habil where anho_des = $1 AND is_active is TRUE AND adelantar is FALSE;
	if found then
		return TRUE;
	end if;
	--Cuando el anho no es activo pero adelantado.
	perform anho_id from referenciales.anho_habil where anho_des = $1 AND is_active is FALSE AND adelantar is TRUE;
	if found then
		return TRUE;
	end if;
	--Si no cumplen las condiciones.
	return FALSE;
end
$$ language plpgsql;