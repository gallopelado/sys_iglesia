from app.Conexion.Conexion import Conexion

class SolicitudHospital:
    def obtenerSolicitantes(self):
        querySQL = '''SELECT ap.adp_id idsolicitante, p.per_nombres nombres, p.per_apellidos apellidos
        FROM membresia.admision_persona ap 
        LEFT JOIN referenciales.personas p ON ap.adp_id = p.per_id 
        WHERE ap.adp_estado IS TRUE '''
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.execute(querySQL)
            return cur.fetchall()
        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()

    def obtenerPacientes(self):
        querySQL = '''SELECT per_id idpersona, per_nombres nombres, per_apellidos apellidos
        FROM referenciales.personas WHERE per_fechabaja is null'''
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.execute(querySQL)
            return cur.fetchall()
        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()

    def obtenerIdiomas(self):
        querySQL = '''SELECT idi_id ididioma, idi_des idioma FROM referenciales.idiomas'''
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.execute(querySQL)
            return cur.fetchall()
        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()