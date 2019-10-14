from app.Conexion.Conexion import Conexion

class ListaCalificadosModel:

    def guardarCalificados(self, idpostulacion, postulantes):
         
        procedimiento = 'membresia.nueva_evaluacion'
        parametros = (idpostulacion, postulantes,)

        try:
            
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.callproc(procedimiento, parametros)
            con.commit()
            return cur.fetchone()[0]

        except con.Error as e:
            print(e.pgerror)
            return False
        finally:
            if con is not None:
                cur.close()
                con.close()


    def obtenerPostulaciones(self):

        funcion = 'membresia.get_postulaciones_para_lista_calificados'

        try:
            
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.callproc(funcion)            
            return cur.fetchall()

        except con.Error as e:
            print(e.pgerror)
            return False
        finally:
            if con is not None:
                cur.close()
                con.close()