from app.Conexion.Conexion import Conexion

class TipoDocumentoModel():

    def listarTodos(self):
        """Metodo listarTodos.

        Obtiene todos los registros de la base de datos
        en formato JSON.

        """
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
        FROM (
            SELECT 
                tdoc_id iddocumento, tdoc_des documento
            FROM
                referenciales.tipo_documento                      
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