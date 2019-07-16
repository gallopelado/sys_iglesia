---------------------------------------
--
-- Procedimiento sp_averiguar_documento
--
---------------------------------------
CREATE OR REPLACE FUNCTION 
    membresia.sp_averiguar_documento(        
        perid integer,
        requisito varchar                
        )
RETURNS boolean AS
/**
*   Procedimiento: sp_averiguar_documento
*   Parámetros:
*   Fecha: 15/07/2019
*   Version: 1.0
*   Autor: Juan José González
*   Email: juanftp100@gmail.com
*   Descripcion: Verifica si la persona tiene algún  
*   documento registrado, retonando TRUE en caso de existencia.
*/
$$
DECLARE
    idpersona integer;
    v_requisito varchar;
	documento_encontrado varchar;
BEGIN
-- Averiguar si el miembro tiene documentos.
--# Setear variables
    idpersona := perid;
    v_requisito := requisito;

    SELECT     
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
        
        --RAISE INFO 'ESTA PERSONA TIENE DOCUMENTOS';

        RETURN true;
    
    END IF;

    RETURN false;    

END;
$$ LANGUAGE plpgsql;
--DROP TYPE membresia.td_averigua_documentos;
--CREATE TYPE membresia.td_averigua_documentos AS (descripcion varchar);
--DROP FUNCTION membresia.sp_averiguar_documentos(perid integer,reqid integer)