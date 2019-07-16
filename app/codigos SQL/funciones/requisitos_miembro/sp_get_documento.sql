---------------------------------------
--
-- Procedimiento sp_get_documento
--
---------------------------------------
CREATE OR REPLACE FUNCTION 
    membresia.sp_get_documento(        
        perid integer,
        requisito varchar                
        )
RETURNS SETOF membresia.td_get_documento AS
/**
*   Procedimiento: sp_get_documento
*   Parámetros: perid integer, requisito
*   Fecha: 15/07/2019
*   Version: 1.0
*   Autor: Juan José González
*   Email: juanftp100@gmail.com
*   Descripcion: Retorna el  
*   documento registrado en formato varchar.
*/
$$
DECLARE
    idpersona integer;
    v_requisito varchar;
	documento_encontrado RECORD;
BEGIN
-- Averiguar si el miembro tiene documentos.
--# Setear variables
    idpersona := perid;
    v_requisito := requisito;
	
    SELECT     
        d.tdoc_id iddocumento,
		t.tdoc_des documento
	INTO
		documento_encontrado
    FROM
	    membresia.documentos_miembro d    
    LEFT JOIN referenciales.tipo_documento t ON
        d.tdoc_id = t.tdoc_id
    WHERE
        d.per_id = idpersona AND t.tdoc_des = v_requisito;
    	
    IF FOUND THEN
        
        RAISE INFO 'ESTA PERSONA TIENE DOCUMENTOS %', documento_encontrado;   
		RETURN NEXT documento_encontrado;
    	
		RETURN;
    END IF;
	
    RAISE WARNING 'NO TIENE DOCUMENTOS';    
	
	RETURN;

END;
$$ LANGUAGE plpgsql;

--CREATE TYPE membresia.td_get_documento AS (id integer, descripcion varchar);
--SELECT * FROM membresia.sp_get_documento(2,'RECOMENDACION');


