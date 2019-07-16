----------------------------------------------------------------------------------------------
--
-- Crear una función que permita insertar tipodocumentos o eventos en referenciales.requisitos.
--
----------------------------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION referenciales.control_requisitos()
RETURNS trigger AS
$$
/**
*   Procedimiento: control_requisitos
*   Autor: Juan José González
*   Fecha: 12/07/2019
*   Versión: 1.0
*   Parametros: sin parámetros.
*   Descripción: Procedimiento que controlará el ingreso de tipodocumentos o eventos,
*   donde solamente uno de ellos podrá persistir.
*/

BEGIN
    
    IF (NEW.tdoc_id is not null AND NEW.eve_id is not NULL) THEN

        RAISE EXCEPTION 'Solamente debe cargarse el tipo de documento o evento' using ERRCODE = '15000';        

    ELSIF (NEW.tdoc_id is NULL AND NEW.eve_id is NULL) THEN

        RAISE EXCEPTION 'No pueden enviarse como NULOS el tipo de documento o evento' using ERRCODE = '15001';       

    END IF;

    RETURN NEW;

END; -- Fin del procedimiento.
$$
LANGUAGE plpgsql;

-----------------------------------------------------------------------------
--
-- Crear el disparador que activa la funcion.
--
-----------------------------------------------------------------------------

-- Definicion del disparador que llama a la funcion anteriormente descrita
CREATE TRIGGER control_requisitos
    BEFORE INSERT OR UPDATE
    ON referenciales.requisitos
    FOR EACH ROW
    EXECUTE PROCEDURE referenciales.control_requisitos();