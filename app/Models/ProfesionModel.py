from app.Conexion.Conexion import Conexion

class ProfesionModel():

    def listarTodos(self):
        """Metodo listarTodos.

        Obtiene todos los registros y retorna lista.

        """

        # SQL
        consulta = "SELECT * FROM referenciales.profesiones;"

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
    
    def guardar(self, op, idpro, descripcion):

        # SQL
        procedimiento = 'referenciales.sp_abmprofesion'

        try:
            
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()

            cur.callproc(procedimiento, (op, idpro, descripcion,))

            con.commit()

            return True

        except con.Error as e:
            print(e.pgerror)
            return False
        finally:
            if con is not None:
                cur.close()
                con.close()