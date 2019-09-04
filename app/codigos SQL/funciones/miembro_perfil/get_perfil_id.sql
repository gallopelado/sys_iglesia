CREATE OR REPLACE FUNCTION membresia.get_perfil_id(id integer)
RETURNS TABLE(idmiembro integer, miembro text, serviren varchar, 
			 cualidadpersonal varchar, actitudminis varchar,
			 antecedentes varchar) as		 
$$
/**
 *	Procedimiento: get_perfil_id
 *	
 *	Descripción: Obtiene un conjunto de datos a partir del idmiembro
 *	de la tabla miembro_perfil. En caso contrario se muestra un
 *	mensaje de tipo INFO y se devuelve una tupla con el registro.
 *	
 *	Parámetros: id integer
 *	Retorna: conjunto de datos(idmiembro integer, miembro text, serviren varchar, 
 *	cualidadpersonal varchar, actitudminis varchar,
 *	antecedentes varchar)
 *	Versión: 1.1	
 *
 *	Autor: Juan José González Ramírez
 *	Emai: juanftp100@gmail.com
 */	
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
	IF not found then
		RETURN QUERY SELECT 
			per_id AS idmiembro,
			per_nombres||' '||per_apellidos AS miembro,
			null::varchar AS serviren, null::varchar AS cualidadpersonal, 
			null::varchar AS actitudminis, null::varchar AS antecendentes
		FROM
			referenciales.personas
		WHERE
			per_id = id;
		RAISE INFO 'NO EXISTE DICHO REGISTRO';
	END IF;

	RETURN;
END;
$$ LANGUAGE plpgsql;
