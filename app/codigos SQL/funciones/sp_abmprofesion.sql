CREATE OR REPLACE FUNCTION referenciales.sp_abmprofesion(op varchar, id integer, descripcion varchar) RETURNS bool AS
$$
BEGIN

    CASE op
        
        WHEN 'a' THEN
            
            INSERT INTO referenciales.profesiones(pro_des) VALUES (UPPER(descripcion));

        WHEN 'b' THEN
        
            DELETE FROM referenciales.profesiones WHERE pro_id = id;

        WHEN 'm' THEN
            
            UPDATE referenciales.profesiones SET pro_des = UPPER(descripcion) WHERE pro_id = id;

        ELSE
            
            RAISE EXCEPTION 'ERROR AL MOMENTO DE HACER LAS OPERACIONES';
            
            RETURN false;
    
    END CASE;

    RETURN true;

END;
$$ LANGUAGE plpgsql;
