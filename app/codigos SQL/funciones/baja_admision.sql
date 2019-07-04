CREATE OR REPLACE FUNCTION membresia.baja_admision(idadmision int, razonbaja razonbaja, obs varchar) RETURNS boolean AS
$$
BEGIN

	--Actualiza el formulario de admision.
	UPDATE membresia.admision_persona 
	SET adp_estado = false, adp_ultimamodif = now() 
	WHERE adp_id = idadmision;

    UPDATE membresia.admision_adicionales
    SET add_estado = false WHERE add_id = idadmision;
	
	--Actualiza la persona.
	UPDATE referenciales.personas 
	SET per_obs = UPPER(obs), per_fechabaja = (SELECT current_date), per_razonbaja = razonbaja
	WHERE per_id = idadmision;
	
	RETURN true;
	
END;
$$ LANGUAGE plpgsql;
