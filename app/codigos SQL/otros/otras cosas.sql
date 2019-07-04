-- Codigo de error personalizado
raise exception 'Ya esta registrado' using ERRCODE = '10004'; 


-- Convierte a un tipo tsvector.
select to_tsvector(per_nombres || ' ' || per_apellidos ) from personas;

-- Consulta con esos elementos.
select per_id, per_nombres || ' ' || per_apellidos as persona from personas
where to_tsvector(per_nombres || ' ' || per_apellidos ) @@ to_tsquery('juan & jose & dimartino');

-- Consulta con esos elementos.
select per_id, per_nombres || ' ' || per_apellidos as persona from personas
where to_tsvector(per_nombres || ' ' || per_apellidos ) @@ to_tsquery((select plainto_tsquery('francisco')::text));


-- Convierte un simple string a un tipo tsquery.
select plainto_tsquery('juan jose');


-- Convierte un valor de tipo TIMESTAMP en TEXT de DD/MM/YYY
select to_char('NOW'::TIMESTAMP WITH TIME ZONE ,'DD/MM/YYYY'::TEXT);
select 'NOW'::TIMESTAMP;

SELECT 
adp.adp_id, per.per_nombres||' '||per.per_apellidos as persona, per.per_ci as cedula,
(select to_char(adp.adp_fecharegistro, 'DD/MM/YYYY'::TEXT))
FROM membresia.admision_persona adp join referenciales.personas per on adp.adp_id=per.per_id;
