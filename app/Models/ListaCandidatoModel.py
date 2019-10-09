from app.Conexion.Conexion import Conexion

class ListaCandidatoModel:

    def traerPostulaciones(self, opcion):

        funcion = 'membresia.get_postulaciones'

        try:
            
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.callproc(funcion, (opcion, ))

        except con.Error as e:
            print(e.pgerror)
            return False
        finally:
            if con is not None:
                cur.close()
                con.close()