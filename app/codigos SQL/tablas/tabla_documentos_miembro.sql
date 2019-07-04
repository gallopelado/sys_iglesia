---------------------------
-- Tabla documentos_miembro
---------------------------
CREATE TABLE 
    membresia.documentos_miembro(
        per_id integer not null primary key,
        tdoc_id integer not null,
        conyuge_id integer,
        doc_oficiador varchar(100),
        doc_documento varchar(150),
        doc_declaracion varchar(200),
        doc_notas varchar(200),
        doc_testigo1 varchar(100),
        doc_testigo2 varchar(100),
        doc_estado bool default true,
        creado_por_usuario integer,
        fecha_modificado timestamp,
        FOREIGN KEY(per_id) REFERENCES referenciales.personas(per_id)
        ON DELETE RESTRICT ON UPDATE CASCADE,
        FOREIGN KEY(tdoc_id) REFERENCES referenciales.tipo_documento(tdoc_id)
        ON DELETE RESTRICT ON UPDATE CASCADE,
        FOREIGN KEY(conyuge_id) REFERENCES referenciales.personas(per_id)
  ); 

-- Modificaciones
-- Eliminar la PK de per_id
ALTER TABLE membresia.documentos_miembro DROP CONSTRAINT documentos_miembro_pkey;
-- Crear constraint para per_id y tdoc_id.A
ALTER TABLE membresia.documentos_miembro ADD PRIMARY KEY(per_id, tdoc_id);
-- Agregar fecha del documento.
ALTER TABLE membresia.documentos_miembro ADD COLUMN doc_fechadocumento date;