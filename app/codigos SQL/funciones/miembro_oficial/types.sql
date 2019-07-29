CREATE TYPE membresia.td_admision_persona AS (
	idadmision integer,
	persona text, 
	fechanacimiento date, 
	direccion varchar, 
	-- #Ciudad
	idciudad integer,
	ciudad varchar,
	-- #Clasificacion social
	idclasisocial integer, 
	clasisocial varchar,
	estadocivil estadocivil, 
	sexo sexo, 
	-- #Relacion familiar
	idrelacionfamiliar integer, 
	relacionfamiliar varchar,
	--#Familia
	idfamilia integer,
	familia varchar,
	fechamatrimonio date, 
	email varchar, 
	postal varchar,
	-- #Forma de contacto
	idformacontacto integer, 
	formacontacto varchar,
	otraiglesia bool, 
	iglesia varchar, 
	fechaprimercontacto date, 
	requierevisita bool, 
	nuevoenciudad bool, 
	ultimavisita date,
	-- #Conyuge
	idconyuge integer,
	conyuge text,
	nrohijos integer, 
	estado bool, 
	ultimamodificacion timestamp, 
	fecharegistro timestamp
);