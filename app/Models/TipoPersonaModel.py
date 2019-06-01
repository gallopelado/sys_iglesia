# Se importa la Clase Conexion
from app.Conexion.Conexion import Conexion

class TipoPersonaModel():

    def listarTiposPersona(self):
        conexion = Conexion()
        con = conexion.getConexion()
        cursor = con.cursor()
        cursor.execute(""" 
            SELECT tipoper_id, tipoper_des
	        FROM referenciales.tipo_persona;
        """)
        lsttipos = cursor.fetchall()
        cursor.close()
        con.close()
        return lsttipos
