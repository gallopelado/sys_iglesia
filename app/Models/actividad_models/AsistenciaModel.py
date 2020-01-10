from app.Conexion.Conexion import Conexion

class AsistenciaModel:

    def procesar(self, opcion, asisid, eveid, asisdes, lista_personas, lista_asistio, lista_puntual):
        funcion = 'actividades.gestionar_asistencia'
        parametros = (opcion, asisid, eveid, asisdes, lista_personas, lista_asistio, lista_puntual,)
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.callproc(funcion, parametros)
            con.commit()
            return cur.fetchone()[0]
        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()

    