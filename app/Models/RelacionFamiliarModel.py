# Se importa clase conexion
from app.Conexion.Conexion import Conexion


class RelacionFamiliarModel():

    def obtenerRelaciones(self):
        conexion = Conexion()
        con = conexion.getConexion()
        cursor = con.cursor()
        cursor.execute(
            """
            SELECT rf_id, rf_des
            FROM referenciales.relacion_familiar; 

            """)
        lista = cursor.fetchall()
        return lista
