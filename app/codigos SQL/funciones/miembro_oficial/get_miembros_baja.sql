--CREATE TYPE membresia.td_miembros_baja AS (idmiembro integer, miembro TEXT, idtipopersona integer, 
--tipopersona varchar, motivo_baja razonbaja);
CREATE OR REPLACE FUNCTION membresia.get_miembros_baja()
RETURNS 
SETOF membresia.td_miembros_baja AS
$$
/**
 * Procedimiento: get_miembros_baja.
 * Descripcion: Obtiene miembros dados de baja.
 * Autor: Juan Jose Gonzalez Ramirez
 * Email: juanftp100@gmail.com
 */
BEGIN
	PERFORM
		m.mo_id AS idmiembro,--integer	
		p.per_nombres ||' '||p.per_apellidos AS miembro, --text
		p.tipoper_id AS idtipopersona,--integer
		tip.tipoper_des AS tipopersona,--varchar
		p.per_razonbaja AS motivo_baja--razonbaja
	FROM
		membresia.miembros_oficiales AS m
	LEFT JOIN
		referenciales.personas AS p ON m.mo_id = p.per_id
	LEFT JOIN
		referenciales.tipo_persona AS tip ON p.tipoper_id = tip.tipoper_id
	WHERE
		p.per_razonbaja IS NOT NULL;
	
	IF NOT FOUND THEN		
		RAISE EXCEPTION 'No existen miembros dados de baja' USING ERRCODE = '15003';
	END IF;

	RETURN QUERY SELECT
		m.mo_id AS idmiembro,--integer	
		p.per_nombres ||' '||p.per_apellidos AS miembro, --text
		p.tipoper_id AS idtipopersona,--integer
		tip.tipoper_des AS tipopersona,--varchar
		p.per_razonbaja AS motivo_baja--razonbaja
	FROM
		membresia.miembros_oficiales AS m
	LEFT JOIN
		referenciales.personas AS p ON m.mo_id = p.per_id
	LEFT JOIN
		referenciales.tipo_persona AS tip ON p.tipoper_id = tip.tipoper_id
	WHERE
		p.per_razonbaja IS NOT NULL;
	
	RETURN;
END;
$$ LANGUAGE plpgsql;
--SELECT * FROM membresia.get_miembros_baja();
--UPDATE referenciales.personas SET per_razonbaja = NULL WHERE per_id = 8;

