# Se importa clase conexion
from app.Conexion.Conexion import Conexion


class ClasificacionSocialModel():

    def obtenerClasificaciones(self):
        conexion = Conexion()
        con = conexion.getConexion()
        cursor = con.cursor()
        cursor.execute(
            """
            SELECT cls_id, cls_des
            FROM referenciales.clasi_social; 

            """)
        lista = cursor.fetchall()
        return lista
