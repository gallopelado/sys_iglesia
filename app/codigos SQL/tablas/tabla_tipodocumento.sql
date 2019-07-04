---------------------------
-- Tabla tipo_documento
---------------------------
CREATE TABLE
    referenciales.tipo_documento(
        tdoc_id serial primary key,
        tdoc_des varchar(100) not null unique
    );

-- INSERCIONES
INSERT INTO referenciales.tipo_documento(tdoc_des)
    VALUES 
    ('MATRIMONIO'),
    ('DEFUNCION'),
    ('RECOMENDACION'),
    ('BAUTISMO'),
    ('TRASLADO'),
    ('EXCOMUNION'), 
    ('INCORPORACION'),
    ('PRESENTACION DE NIÑO'), 
    ('OTROS');
