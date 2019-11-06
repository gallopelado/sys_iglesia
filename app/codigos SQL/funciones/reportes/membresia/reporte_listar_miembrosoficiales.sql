CREATE OR REPLACE FUNCTION membresia.reporte_listar_miembrosoficiales(
	fechadesde date, fechahasta date, requisito varchar, sexo sexo, civil estadocivil, mes varchar
) RETURNS 
	table(idmiembro integer, miembro text, sexo sexo, ecivil estadocivil, fechanac text, fechainiciomembresia text,
		  estado membresia.estado_membresia,
		idrazonalta integer, requisito varchar
	) AS
$$

		SELECT
			mie.mo_id idmiembro,
			per.per_nombres || ' ' || per.per_apellidos AS miembro,
			admi.adp_sexo sexo,
			admi.adp_ecivil ecivil,
			fecha_formatolargo(admi.adp_fechanac) fechanac,
			fecha_formatolargo(mie.mo_fechainiciomembresia) fechainiciomembresia,
			mie.mo_estadomembresia estado,
			mie.razonalta_id idrazonalta,
			req.req_des requisito
		FROM
			membresia.miembros_oficiales AS mie
		LEFT JOIN 
			referenciales.personas AS per ON mie.mo_id = per.per_id
		LEFT JOIN
			referenciales.requisitos AS req ON mie.razonalta_id = req.req_id
		LEFT JOIN membresia.admision_persona AS admi ON mie.mo_id = admi.adp_id
		WHERE	
			per.per_razonbaja IS NULL AND
			  
			CASE WHEN fechadesde IS NOT NULL THEN
				CASE WHEN fechahasta IS NOT NULL THEN
					mo_fechainiciomembresia BETWEEN fechadesde AND fechahasta
				ELSE
					TRUE
				END
			ELSE
				TRUE
			END
			AND
			CASE WHEN LENGTH(requisito) > 0 THEN				
				req.req_des = requisito 
			ELSE
				TRUE
			END
			AND
			CASE WHEN sexo IS NOT NULL THEN
				admi.adp_sexo = sexo 
			ELSE
				TRUE
			END
			AND
			CASE WHEN civil IS NOT NULL THEN
				admi.adp_ecivil = civil
			ELSE
				TRUE
			END
			AND
			CASE WHEN mes IS NOT NULL THEN
				trae_mes(admi.adp_fechanac) = UPPER(mes)
			ELSE
				TRUE
			END;
$$ LANGUAGE SQL;
