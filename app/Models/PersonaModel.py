# Se importa la Clase Conexion
from app.Conexion.Conexion import Conexion


class PersonaModel():
    """Clase PersonaModel.

    Se encuentra definiciones que se relaciona 
    con la base de datos con el modelo Persona.

    """
    
    def listarPersonas(self):
        """Metodo listarPersonas.

        Se encarga de obtener todas las personas con su tipo.

        Retorna: 
            lstpersona: -- tupla

        """
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cursor = con.cursor()
            cursor.execute(
                """SELECT p.per_id, p.per_ci, p.per_nombres, p.per_apellidos, p.tipoper_id, t.tipoper_des, p.per_obs
	            FROM referenciales.personas p
	            join referenciales.tipo_persona t on p.tipoper_id=t.tipoper_id; 
                """)
            lstpersona = cursor.fetchall()
            cursor.close()
            con.close()
            return lstpersona
        except con.Error as e:
            print(e.pgerror)    

    def guardar(self, op, perid, perci, pernombres, perapellidos, tipo, perobs):
        """Metodo guardar.

        Se encarga persistir los datos en la base de datos

        Retorna: 
            estado: -- booleano

        """
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cursor = con.cursor()
            cursor.execute(
                """
                SELECT referenciales.sp_abmpersona(%s, %s, %s, %s, %s, %s, %s);
                """,
                (op, perid, perci, pernombres, perapellidos, tipo, perobs))
            # Realizar cambios
            con.commit()

            # Cerrar la comunicacion con la BD
            cursor.close()
            con.close()

            return True
        except con.Error as e:
            print(e.pgerror)  

    def recuperaPersona(self, idpersona):
        """Metodo recuperaPersona.

        Obtiene un registro segun id de persona, con todos los datos.

        Retorna: 
            persona: -- diccionario

        """
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cursor = con.cursor()
            cursor.execute("""
            SELECT p.per_id, p.per_ci, p.per_nombres, p.per_apellidos, p.tipoper_id, p.per_obs, p.per_fechabaja, p.per_razonbaja, tp.tipoper_des 
            FROM referenciales.personas p 
            join referenciales.tipo_persona tp on p.tipoper_id=tp.tipoper_id
            WHERE per_id = %s;
            """,(idpersona,))
            data = cursor.fetchone()
            cursor.close()
            con.close()
            return data
        except con.Error as e:
            return e.pgerror
        
    def recuperaPersonas(self):
        """Metodo recuperaPersonas.

        Obtiene registros de persona, con todos los datos.

        Retorna: 
            personas: -- diccionario

        """
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cursor = con.cursor()
            cursor.execute("""
            SELECT p.per_id, p.per_ci, p.per_nombres, p.per_apellidos, p.tipoper_id, tp.tipoper_des, p.per_obs, p.per_fechabaja, p.per_razonbaja 
            FROM referenciales.personas p 
            join referenciales.tipo_persona tp on p.tipoper_id=tp.tipoper_id
            """)
            persona = cursor.fetchall()
            cursor.close()
            con.close()
            return persona
        except con.Error as e:
            return e.pgerror
