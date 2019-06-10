# Se importa clase conexion
from app.Conexion.Conexion import Conexion


class FormaContactoModel():

    def obtenerFormas(self):
        conexion = Conexion()
        con = conexion.getConexion()
        cursor = con.cursor()
        cursor.execute(
            """
            SELECT foc_id, foc_des
            FROM referenciales.forma_contacto;

            """)
        lista = cursor.fetchall()
        return lista
