/**
* Función documentos_miembro
* Parámetros: opcion integer,          
        idpersona integer
        idtipodocumento integer,
        idconyuge integer,
        oficiador varchar,
        documento varchar,
        declaracion varchar,
        notas varchar,
        testigo1 varchar,
        testigo2 varchar,
        fechadoc date,
        estado boolean,        
        usuario integer
* Versión: 0.1
* Fecha: 04/07/2019
* Autor: Juan José González Ramírez <juanftp100@gmail.com>
* Descripción: ABM de la tabla.
*
*/

CREATE OR REPLACE FUNCTION 
    membresia.sp_documentos_miembro(
        opcion varchar,          
        idpersona integer,
        idtipodocumento integer,
        idconyuge integer,
        oficiador varchar,
        documento varchar,
        declaracion varchar,
        notas varchar,
        testigo1 varchar,
        testigo2 varchar,
        fechadoc date,
        estado boolean,        
        usuario integer                
         )
RETURNS BOOLEAN AS
$$
    DECLARE
        -- Se declaran una variable de tipo ROWTYPE de la tabla.
        temp_row membresia.documentos_miembro%ROWTYPE;
    
    BEGIN

        -- Asignar y Sanear las variables
        temp_row.per_id := idpersona;
        temp_row.tdoc_id := idtipodocumento;
        temp_row.doc_oficiador := null;
        temp_row.doc_documento := null;
        temp_row.doc_declaracion := null;
        temp_row.doc_notas := null;
        temp_row.doc_testigo1 := null;
        temp_row.doc_testigo2 := null;
        temp_row.doc_fechadocumento := null;

        -- Asignar usuario.
        temp_row.creado_por_usuario := null;

        IF oficiador IS NOT NULL THEN

             temp_row.doc_oficiador := TRIM(UPPER(oficiador));
        
        END IF;

        IF documento IS NOT NULL THEN

            temp_row.doc_documento := TRIM(documento);

        END IF;

        IF declaracion IS NOT NULL THEN

            temp_row.doc_declaracion := TRIM(UPPER(declaracion));

        END IF;

        IF notas IS NOT NULL THEN

            temp_row.doc_notas := TRIM(UPPER(notas));

        END IF;

        IF testigo1 IS NOT NULL THEN

            temp_row.doc_testigo1 := TRIM(UPPER(testigo1));

        END IF;

        IF testigo2 IS NOT NULL THEN

            temp_row.doc_testigo2 := TRIM(UPPER(testigo2));

        END IF;

        IF fechadoc IS NOT NULL THEN

            temp_row.doc_fechadocumento := fechadoc;

        END IF;

        CASE 
            -- Alta
            WHEN opcion = 'a' THEN

                -- Asigna fecha de modificacion null.
                temp_row.fecha_modificado := null;
                temp_row.doc_estado := true;

                -- Insertar
                INSERT INTO 
                    membresia.documentos_miembro(
                        per_id,
                        tdoc_id,
                        conyuge_id,
                        doc_oficiador,
                        doc_documento,
                        doc_declaracion,
                        doc_notas,
                        doc_testigo1,
                        doc_testigo2,
                        doc_estado,
                        creado_por_usuario,
                        fecha_modificado,
                        doc_fechadocumento
                    )
                VALUES (
                    temp_row.*
                );
            
                RAISE NOTICE 'INSERTASTE en documentos_miembro';
                RETURN TRUE;

            -- Baja
            WHEN opcion = 'b' THEN

                -- Asigna fecha de modificacion y estado.
                temp_row.fecha_modificado := NOW();
                temp_row.doc_estado := FALSE;

                -- Realizar UPDATE
                UPDATE 
                    membresia.documentos_miembro
                SET
                    doc_estado = temp_row.doc_estado,
                    fecha_modificado = temp_row.fecha_modificado
                WHERE
                    per_id = temp_row.per_id AND tdoc_id = temp_row.tdoc_id;
                
                RAISE NOTICE 'SE DIO DE BAJA documentos_miembros';
                RETURN TRUE;

            -- Modificación
            WHEN opcion = 'm' THEN

                -- Asigna fecha de modificacion y estado.
                temp_row.fecha_modificado := NOW();
                temp_row.doc_estado := TRUE;

                -- Realizar UPDATE
                UPDATE 
                    membresia.documentos_miembro
                SET
                    (conyuge_id, doc_oficiador, doc_documento, doc_declaracion, 
                    doc_notas, doc_testigo1, doc_testigo2, doc_estado, creado_por_usuario, 
                    fecha_modificado, doc_fechadocumento) = (
                        temp_row.conyuge_id, temp_row.doc_oficiador, temp_row.doc_documento, temp_row.doc_declaracion,
                        temp_row.doc_notas, temp_row.doc_testigo1, temp_row.doc_testigo2, temp_row.doc_estado,
                        temp_row.creado_por_usuario, temp_row.fecha_modificado, temp_row.doc_fechadocumento)

                WHERE
                    per_id = temp_row.per_id AND tdoc_id = temp_row.tdoc_id;
                
                RAISE NOTICE 'SE REALIZO LA ACTUALIZACION documentos_miembros';
                RETURN TRUE;

            END CASE;

            RETURN FALSE;

    END;    
$$    LANGUAGE plpgsql;


-- Ejemplo de insercion.
/*

SELECT membresia.sp_documentos_miembro(
	'a', 
	2, 
	3, 
	null, 
	'efrain mencia', 
	'certi.jpg', 
	'null', 
	'null', 
	'Celina Ramirez', 
	null, 
	(SELECT CURRENT_DATE), 
	true, 
	null
)


*/