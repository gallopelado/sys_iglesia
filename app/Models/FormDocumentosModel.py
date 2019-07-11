from app.Conexion.Conexion import Conexion

class FormDocumentosModel():

    def listarMiembrosDocumentos(self):
        """listarMiembrosDocumentos.

        Obtiene una lista en formato JSON.

        """
        # SQL
        consulta = """

        SELECT 
            array_to_json(
                array_agg(
                    row_to_json(
                        data
                    )
                )
            )
        FROM
	        (
            SELECT
                d.per_id idmiembro,
                p.per_nombres||' '||p.per_apellidos persona,
                d.tdoc_id idtipodocumento,
                t.tdoc_des documento,
                d.doc_fechadocumento fechadocumento
            FROM
                membresia.documentos_miembro d
                LEFT JOIN referenciales.personas p ON
                d.per_id = p.per_id
                LEFT JOIN referenciales.tipo_documento t ON
                d.tdoc_id = t.tdoc_id
            WHERE
                d.doc_estado = true

	        ) data;

        """
        try:
            
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.execute(consulta)
            return cur.fetchall()            

        except con.Error as e:
            print(e.pgerror)
            return False
        finally:
            if con is not None:
                cur.close()
                con.close()

    def obtenerMiembroDocumento(self, idmiembro, idtipodocumento):

        # SQL
        consulta = """

        SELECT
            ARRAY_TO_JSON(
                ARRAY_AGG(
                    ROW_TO_JSON(
                        data
                    )
                )
            )
        FROM 
            (
                SELECT
                    d.per_id idmiembro,
                    p.per_nombres||' '||p.per_apellidos persona,
                    d.tdoc_id idtipodocumento,
                    t.tdoc_des documento,
                    d.conyuge_id,
                    p2.per_nombres||' '||p2.per_apellidos conyuge,
                    d.doc_oficiador oficiador,
                    d.doc_documento archivo,
                    d.doc_declaracion declaracion,
                    d.doc_notas notas,
                    d.doc_testigo1 testigo1,
                    d.doc_testigo2 testigo2,
                    d.doc_fechadocumento fechadocumento
                FROM
                    membresia.documentos_miembro d
                    LEFT JOIN referenciales.personas p ON
                    d.per_id = p.per_id
                    LEFT JOIN referenciales.tipo_documento t ON
                    d.tdoc_id = t.tdoc_id
                    LEFT JOIN referenciales.personas p2 ON
                    d.conyuge_id = p2.per_id
                WHERE 
                    d.per_id = %s AND d.tdoc_id = %s
            ) data;

        """
        parametros = (idmiembro, idtipodocumento,)
        try:
            
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.execute(consulta, parametros)
            return cur.fetchone()

        except con.Error as e:
            print(e.pgerror)
            return False
        finally:
            if con is not None:
                cur.close()
                con.close()

    def guardar(self, idtipodocumento, txt_fecha, idmiembro, idconyuge, oficiador,
                documento, declaracion, notas, testigo1, testigo2):
        """Metodo guardar.

        Guarda datos del formulario de datos adicionales.

        """
        #SQL
        procedimiento = "membresia.sp_documentos_miembro"
        parametros = ('a', idmiembro, None, idtipodocumento, idconyuge, oficiador, 
                        documento, declaracion, notas, testigo1, testigo2, 
                        txt_fecha, None, None)
        try:
            
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.callproc(procedimiento, parametros)

            con.commit()

            return True

        except con.Error as e:
            print(e.pgerror)
            return False
        finally:
            if con is not None:
                cur.close()
                con.close()

    def modificar(self, id_antiguo_tipodocumento, idtipodocumento, txt_fecha, idmiembro, idconyuge, oficiador,
                documento, declaracion, notas, testigo1, testigo2):
        """Metodo modificar.

        Modifica datos del formulario de datos adicionales.

        """
        #SQL
        procedimiento = "membresia.sp_documentos_miembro"
        parametros = ('m', idmiembro, id_antiguo_tipodocumento, idtipodocumento, idconyuge, oficiador,
                      documento, declaracion, notas, testigo1, testigo2,
                      txt_fecha, None, None)
        try:

            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.callproc(procedimiento, parametros)

            con.commit()

            return True

        except con.Error as e:
            print(e.pgerror)
            return False
        finally:
            if con is not None:
                cur.close()
                con.close()

    def eliminar(self, idmiembro, idtipodocumento):

       #SQL
        procedimiento = "membresia.sp_documentos_miembro"
        parametros = ('b', idmiembro, None, idtipodocumento, None, None,
                      None, None, None, None, None,
                      None, None, None)
        try:

            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.callproc(procedimiento, parametros)

            con.commit()

            return True

        except con.Error as e:
            print(e.pgerror)
            return False
        finally:
            if con is not None:
                cur.close()
                con.close()
