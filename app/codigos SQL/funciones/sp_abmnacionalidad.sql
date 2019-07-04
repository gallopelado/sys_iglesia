CREATE OR REPLACE FUNCTION referenciales.sp_abmnacionalidad(op varchar, id integer, descripcion varchar) RETURNS bool AS
$$
BEGIN

    CASE op
        
        WHEN 'a' THEN
            
            INSERT INTO referenciales.nacionalidad(nac_des) VALUES (UPPER(descripcion));

        WHEN 'b' THEN
        
            DELETE FROM referenciales.nacionalidad WHERE nac_id = id;

        WHEN 'm' THEN
            
            UPDATE referenciales.nacionalidad SET nac_des = UPPER(descripcion) WHERE nac_id = id;

        ELSE
            
            RAISE EXCEPTION 'ERROR AL MOMENTO DE HACER LAS OPERACIONES';
            
            RETURN false;
    
    END CASE;

    RETURN true;

END;
$$ LANGUAGE plpgsql;
