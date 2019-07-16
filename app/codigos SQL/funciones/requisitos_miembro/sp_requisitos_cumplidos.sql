---------------------------------------
--
-- Procedimiento requisitos_cumplidos
--
---------------------------------------
CREATE OR REPLACE FUNCTION 
    sp_requisitos_cumplidos(
        op varchar,
        perid integer,
        reqid integer,
        obs text        
        )
RETURNS BOOLEAN AS
/**
*   Procedimiento: sp_requisitos_cumplidos
*   Parámetros:
*   Fecha: 12/07/2019
*   Version: 1.0
*   Autor: Juan José González
*   Email: juanftp100@gmail.com
*   Descripcion: Registrar o modificar los requisitos de los 
*   miembros.
*/
$$
-- A tener en cuenta,
-- Para insertar en requisitos_cumplidos, el miembro debe tener por lo menos
-- alguno de los cuatro documentos importantes. Son:
-- RECOMENDACION, BAUTISMO, TRASLADO, TESTIMONIO.
-- Adicionalmente se podrá añadir los eventos a donde asistió. Especialmente en
-- TESTIMONIO.
DECLARE
    opcion varchar;
    temp_row membresia.requisitos_cumplidos%ROWTYPE;
BEGIN
-- SETEAR Y SANEAR.
    opcion := op;
    temp_row.per_id := perid;
    temp_row.req_id := reqid;
    temp_row.fecha := now();
    temp_row.observacion := TRIM(UPPER(obs));
-- ALTA
-- Averiguar si el miembro tiene documentos.
    PERFORM sp_averiguar_documentos(perid, reqid);
    IF FOUND THEN

        

    END IF;
END;
$$
    LANGUAGE plpgsql;