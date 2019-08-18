CREATE OR REPLACE FUNCTION membresia.reincorporar_miembro(idadmision int, obs varchar) RETURNS boolean AS
$$
/**
 * Procedimiento: reincorporar_miembro
 * Descripción: Reincorpora un miembro oficial.
 * Parámetros: idadmision, obs
 * Versión: 1.0
 * Autor: Juan José González Ramírez
 * Email: juanftp100@gmail.com
 */
DECLARE
	--Variables de fecha actual.
	v_fechaactual_timest TIMESTAMP := now();
	v_fechaactual_date DATE := (SELECT CURRENT_DATE);
BEGIN

	--Actualiza el formulario de admision.
	UPDATE 
		membresia.admision_persona 
	SET 
		adp_estado = true, adp_ultimamodif = v_fechaactual_timest 
	WHERE 
		adp_id = idadmision;

	--Actualiza formulario adicionales.
    UPDATE 
    	membresia.admision_adicionales
    SET 
   		add_estado = true 
   	WHERE 
   		add_id = idadmision;
	
	--Actualiza la persona.
	UPDATE 
		referenciales.personas 
	SET 
		per_obs = UPPER(TRIM(obs)), per_fechabaja = null, per_razonbaja = NULL, 
		per_fechareincorporacion = v_fechaactual_date
	WHERE 
		per_id = idadmision;
	
	RETURN true;
	
END;
$$ LANGUAGE plpgsql;
