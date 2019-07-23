from app.Conexion.Conexion import Conexion


class RequisitoModel():

    def listarTodo(self):

        # SQL
        procedimiento = "referenciales.obtener_todos_requisitos_json"

        try:
            
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.callproc(procedimiento)
            return cur.fetchone()

        except con.Error as e:
            print(e.pgerror)
            return False
        finally:
            if con is not None:
                cur.close()
                con.close()
    
    def listarPersonasActivas(self):

        # SQL
        procedimiento = "referenciales.get_personas_activas"

        try:
            
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.callproc(procedimiento)
            return cur.fetchall()

        except con.Error as e:
            print(e.pgerror)
            return False
        finally:
            if con is not None:
                cur.close()
                con.close()