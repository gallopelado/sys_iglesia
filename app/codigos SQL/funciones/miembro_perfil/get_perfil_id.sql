CREATE OR REPLACE FUNCTION membresia.get_perfil_id(id integer)
RETURNS TABLE(idmiembro integer, miembro text, serviren varchar, 
			 cualidadpersonal varchar, actitudminis varchar,
			 antecedentes varchar) AS
$$
BEGIN
	RETURN QUERY SELECT 
		m.mper_id as idmiembro,
		p.per_nombres||' '||p.per_apellidos as miembro,
		m.mper_serviren as serviren, 
		m.mper_cualipers as cualidadpersonal, 
		m.mper_actiminis as actitudminis, 
		m.mper_anteced as antecedentes
	FROM 
		membresia.miembro_perfil as m
	LEFT JOIN  
		referenciales.personas as p ON m.mper_id = p.per_id
	WHERE
		m.mper_id = id;
	IF not found THEN
		RAISE EXCEPTION 'NO EXISTE DICHO REGISTRO';
	END IF;
	RETURN;
END;
$$ LANGUAGE plpgsql;
/*
Quiero:
idmiembro, miembro, donde quiere servir, cualidad, actitud ministerial,
antecedentes.
*/