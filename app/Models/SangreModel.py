from app.Conexion.Conexion import Conexion

class SangreModel():

    def listarTodos(self):
        """Metodo listarTodos.

        Obtiene todos los registros y retorna lista.

        """

        #SQL
        consulta = "SELECT * FROM referenciales.sangre;"
        
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