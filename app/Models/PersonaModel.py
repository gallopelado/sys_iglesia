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
                """

                    SELECT p.per_id, p.per_ci, p.per_nombres, p.per_apellidos, p.tipoper_id, t.tipoper_des, p.per_obs,
                    p.per_razonbaja,  p.per_fechabaja,
                    case p.per_razonbaja 
                    when nullif(p.per_razonbaja, null) then 
	                    'INACTIVO'	
                    else
	                    'ACTIVO'
                    end
                    as estado
                    FROM referenciales.personas p
                    join referenciales.tipo_persona t on p.tipoper_id=t.tipoper_id;

                """)
            lstpersona = cursor.fetchall()
            cursor.close()
            con.close()
            return lstpersona
        except con.Error as e:
            print(e.pgerror)

    # Para AJAX
    def listarPersonasJSON(self):
        """Metodo listarPersonas.

        Obtiene lista de personas en formato JSON.

        """
        consulta = """

        SELECT ARRAY_TO_JSON(
                ARRAY_AGG(
                    ROW_TO_JSON(
                        data
                    ) 
                )
            )
        FROM 
            (
                SELECT
                    per_id idpersona,
                    per_nombres ||' '|| per_apellidos persona
                FROM
                    referenciales.personas
                WHERE
                    per_fechabaja IS NULL 
            ) data;
        
        """

        try:
            
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.execute(consulta)

            return cur.fetchall()            

        except con.Error as e:
            print(e.pgerror)
            return False
        finally:
            if con is not None:
                cur.close()
                con.close()

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
            """, (idpersona,))
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
        consultaOLD = """ 
        
            SELECT p.per_id, p.per_ci, p.per_nombres, p.per_apellidos, p.tipoper_id, tp.tipoper_des, p.per_obs, p.per_fechabaja, p.per_razonbaja
            FROM referenciales.personas p
            LEFT JOIN referenciales.tipo_persona tp on p.tipoper_id=tp.tipoper_id
            WHERE p.per_fechabaja IS null

        """
        # Solamente obtiene los registros que no tienen formulario de admision.
        consultaNEW = """
        
            SELECT p.per_id, p.per_ci, p.per_nombres, p.per_apellidos, p.tipoper_id, tp.tipoper_des, p.per_obs, p.per_fechabaja, p.per_razonbaja
            FROM referenciales.personas p
            LEFT JOIN referenciales.tipo_persona tp on p.tipoper_id=tp.tipoper_id
            left outer join membresia.admision_persona ad on p.per_id = ad.adp_id
            WHERE (p.per_fechabaja IS null) and (ad.adp_id is null) and (tp.tipoper_id=2);
        
        """
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cursor = con.cursor()
            cursor.execute(consultaNEW)
            persona = cursor.fetchall()
            cursor.close()
            con.close()
            return persona
        except con.Error as e:
            return e.pgerror

    def recuperaPadres(self):
        """Metodo recuperaPersonas.

        Obtiene registros de persona, con todos los datos.

        Retorna:
            personas: -- diccionario

        """
        consultaOLD = """ 
        
            SELECT p.per_id, p.per_ci, p.per_nombres, p.per_apellidos, p.tipoper_id, tp.tipoper_des, p.per_obs, p.per_fechabaja, p.per_razonbaja
            FROM referenciales.personas p
            LEFT JOIN referenciales.tipo_persona tp on p.tipoper_id=tp.tipoper_id
            WHERE p.per_fechabaja IS null

        """
        # Solamente obtiene los registros que no tienen formulario de admision.
        consultaNEW = """
        
            SELECT p.per_id, p.per_ci, p.per_nombres, p.per_apellidos, p.tipoper_id, tp.tipoper_des, p.per_obs, p.per_fechabaja, p.per_razonbaja
            FROM referenciales.personas p
            LEFT JOIN referenciales.tipo_persona tp on p.tipoper_id=tp.tipoper_id
            left outer join membresia.admision_persona ad on p.per_id = ad.adp_id
            WHERE (p.per_fechabaja IS null) and (ad.adp_id is null) and (tp.tipoper_id=2);
        
        """
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cursor = con.cursor()
            cursor.execute(consultaOLD)
            persona = cursor.fetchall()
            cursor.close()
            con.close()
            return persona
        except con.Error as e:
            return e.pgerror

    # Metodo estatico usando diccionario
    @staticmethod
    def verificarPersona(nombres, apellidos):

        # print(f"debug: nombre {nombres}, apellido {apellidos}")

        try:
            # Imprimo parametros
            # print(nombres, apellidos)
            conexion = Conexion()
            con = conexion.getConexion()
            cursor = con.cursor()
            sql = f"SELECT * FROM referenciales.personas p WHERE p.per_nombres = '{nombres}' AND p.per_apellidos = '{apellidos}'"
            # print(f"debug {sql}")

            cursor.execute(sql)

            encontrado = cursor.fetchone()
            # print(encontrado)

            # print(encontrado)
            cursor.close()
            con.close()
            if encontrado:

                return encontrado

            else:
                return False

        except con.Error as e:
            print(e.pgerror)
            return e.pgerror

    # Usando segun la guia oficial
    def verificarPersona2(self, nombres, apellidos):

        try:

            consulta = """
            
            SELECT * FROM referenciales.personas
            WHERE per_nombres = %s AND per_apellidos = %s 
            
            """
            conexion = Conexion()
            con = conexion.getConexion()

            cursor = con.cursor()
            cursor.execute(consulta, (nombres, apellidos,))

            lista = cursor.fetchone()
            print(lista)

        except con.Error as e:
            print(e.pgerror)
