from app.Conexion.Conexion import Conexion

class FormDocumentosModel():

    def guardar(self, idtipodocumento, txt_fecha, idmiembro, idconyuge, oficiador,
                documento, declaracion, notas, testigo1, testigo2):
        """Metodo guardar.

        Guarda datos del formulario de datos adicionales.

        """
        #SQL
        procedimiento = "membresia.sp_documentos_miembro"
        parametros = ('a', idmiembro, idtipodocumento, idconyuge, oficiador, 
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
