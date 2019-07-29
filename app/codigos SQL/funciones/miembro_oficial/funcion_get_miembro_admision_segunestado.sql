CREATE OR REPLACE FUNCTION membresia.get_miembro_admision(bool) 
RETURNS SETOF membresia.td_admision_persona AS
$$
/**
*   Funcion: get_miembro_admision
*   Descripción: Obtiene todos los registros de la tabla admision_persona,
*   con sus joins respectivos según parametros.
* 	Parámetros: estado.
*/    
SELECT 
	ad.adp_id idadmision,
	p.per_nombres||' '||p.per_apellidos persona, 
	ad.adp_fechanac fechanacimiento, 
	ad.adp_direccion direccion, 
	-- #Ciudad
	ad.ciu_id idciudad,
	c.ciu_des ciudad,
	-- #Clasificacion social
	ad.cls_id idclasisocial, 
	cls.cls_des clasisocial,
	ad.adp_ecivil estadocivil, 
	ad.adp_sexo sexo, 
	-- #Relacion familiar
	ad.rf_id idrelacionfamiliar, 
	rf.rf_des relacionfamiliar,
	--#Familia
	ad.fa_id idfamilia,
	fa.fa_des familia,
	ad.adp_fechamatri fechamatrimonio, 
	ad.adp_email email, 
	ad.adp_postal postal,
	-- #Forma de contacto
	ad.foc_id idformacontacto, 
	fc.foc_des formacontacto,
	ad.adp_otraiglesia otraiglesia, 
	ad.adp_iglesia iglesia, 
	ad.adp_fechaprimercontacto fechaprimercontacto, 
	ad.adp_requierevisita requierevisita, 
	ad.adp_nuevoenciudad nuevoenciudad, 
	ad.adp_ultimavisita ultimavisita,
	-- #Conyuge
	ad.conyuge_id idconyuge,
	cony.per_nombres || ' ' || cony.per_apellidos conyuge,
	ad.adp_nrohijos nrohijos, 
	ad.adp_estado estado, 
	ad.adp_ultimamodif ultimamodificacion, 
	ad.adp_fecharegistro fecharegistro
FROM 
	membresia.admision_persona ad
LEFT JOIN
	referenciales.personas p ON ad.adp_id = p.per_id
INNER JOIN
	referenciales.ciudades c ON ad.ciu_id = c.ciu_id
INNER JOIN
	referenciales.clasi_social cls ON ad.cls_id = cls.cls_id
INNER JOIN 
	referenciales.relacion_familiar rf ON ad.rf_id = rf.rf_id
INNER JOIN
	referenciales.familias fa ON ad.fa_id = fa.fa_id
INNER JOIN
	referenciales.forma_contacto fc ON ad.foc_id = fc.foc_id
LEFT JOIN
	referenciales.personas cony ON ad.conyuge_id = cony.per_id
WHERE
	ad.adp_estado = $1
$$ LANGUAGE SQL;

--SELECT * FROM membresia.get_miembro_admision(false);
--SELECT (membresia.get_miembro_admision(false)).estado;
