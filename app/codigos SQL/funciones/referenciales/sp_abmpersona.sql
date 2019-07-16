--SELECT per_id, per_ci, per_nombres, per_apellidos, tipoper_id, per_obs, per_fechabaja, per_razonbaja
--	FROM referenciales.personas;
create or replace function referenciales.sp_abmpersona(
	op varchar, perid integer, perci varchar, pernombres varchar, perapellidos varchar, 
	tipoperid integer, perobs varchar)
	returns boolean as
$$
begin
	--Casos
	case 
		--Alta
		-- Con mantener personas solamente debe darse de alta un registro de tipo visitante, otros procesos
		-- se encargan de cambiar el tipo de persona.
		when op = 'a' then
			INSERT INTO referenciales.personas(
			per_ci, per_nombres, per_apellidos, tipoper_id, per_obs)
			VALUES (trim(perci), UPPER(trim(pernombres)), UPPER(trim(perapellidos)), 2, UPPER(trim(perobs));
			return true;
		
		--Modificacion
		-- Con mantener personas no puede modificarse el tipo de persona, otros procesos se encargan de el.
		when op = 'm' then
			UPDATE referenciales.personas
			SET per_ci=trim(perci), UPPER(trim(pernombres)), per_apellidos=UPPER(trim(perapellidos)), per_obs=UPPER(trim(perobs))
			WHERE per_id=perid;
			return true;
			
		-- Baja
		--- Con mantener personas solamente debe eliminar aquellos registros que no estan siendo usados por otras tablas, referenciados.
		when op = 'b' then
			DELETE FROM referenciales.personas
			WHERE per_id=perid;
			return true;
		
		-- Por defecto
		ELSE
			raise EXCEPTION 'Ninguna opción ingresada es válida';
			RETURN FALSE;
	end case;
	
end
$$
language plpgsql;
										
