from app.Conexion.Conexion import Conexion

class ActividadAnualModel:

    def obtenerAnho(self):
        try:
            consulta = 'select anho_id idanho, anho_des anho, is_active activo from referenciales.anho_habil'
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.execute(consulta)
            return cur.fetchall()
        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()
