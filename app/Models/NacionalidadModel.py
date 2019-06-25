from app.Conexion.Conexion import Conexion

class NacionalidadModel():

    def listarTodos(self):
        """Metodo listarTodos().

        Obtiene tuplas de los registros de nacionalidad del modelo.

        """
        # SQL
        consulta = "SELECT * FROM referenciales.nacionalidad"

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
    
    