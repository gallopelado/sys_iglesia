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

    def getDataPersonaRequisito(self, idpersona):
        """Funcion getDataPersonaRequisito.
            * Descripcion: Según id de persona, se debe obtener
            * nombre y apellido del sujeto, requisito ligados al registro
            * con su id, descripción, observacion.(Personas sin fecha de baja y razon.)
        """
        # SQL
        procedimiento = "membresia.get_data_persona_requisito"

        try:
            
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.callproc(procedimiento, (idpersona,))
            return cur.fetchall()

        except con.Error as e:
            print(e.pgerror)
            return False
        finally:
            if con is not None:
                cur.close()
                con.close()

    def getNombre(self, idpersona):
        
        procedimiento = "referenciales.get_personas"

        try:
            
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.callproc(procedimiento, (idpersona,))
            return cur.fetchone()
            
        except con.Error as e:
            print(e.pgerror)
            return False
        finally:
            if con is not None:
                cur.close()
                con.close()
    
    def guardar(self, idpersona, idrequisitos, observaciones):
        
        # SQL
        procedimiento = "membresia.persona_requisitos"

        try:
        
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.callproc(procedimiento, (idpersona, idrequisitos, observaciones, None, ))
            con.commit()
            return True

        except con.Error as e:
            print(e.pgerror)
            return False
        finally:
            if con is not None:
                cur.close()
                con.close()
