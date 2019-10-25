from app.Conexion.Conexion import Conexion

class ComiteModel:

    def traerTodos(self):

        consultaSQL = '''
        SELECT
            c.min_id idcomite
            , m.min_des descripcion
            , p.per_nombres ||' '|| p.per_apellidos lider
        FROM
            membresia.comites AS c
        LEFT JOIN 
            referenciales.ministerios AS m ON c.min_id = m.min_id
        LEFT JOIN 
            referenciales.personas AS p ON c.lider_id = p.per_id
        WHERE
            c.com_estado IS true        
        '''

        try:
            
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.execute(consultaSQL)
            return cur.fetchall()

        except con.Error as e:
            print(e.pgerror)
            return False
        finally:
            if con is not None:
                cur.close()
                con.close()

    
    def traerPorId(self, idcomite):
        consultaSQL = '''
        SELECT
            c.min_id idcomite
            , m.min_des comite
            , c.lider_id idlider
            , p.per_nombres ||' '|| p.per_apellidos lider
            , c.suplente_id idsuplente
            , sup.per_nombres ||' '|| sup.per_apellidos suplente
            , c.com_des descripcion
            , c.com_obs observacion
        FROM
            membresia.comites AS c
        LEFT JOIN 
            referenciales.ministerios AS m ON c.min_id = m.min_id
        LEFT JOIN 
            referenciales.personas AS p ON c.lider_id = p.per_id
        LEFT JOIN referenciales.personas AS sup ON c.suplente_id = sup.per_id
        WHERE
            c.com_estado IS TRUE AND c.min_id = %s     
        '''

        try:
            
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.execute(consultaSQL, (idcomite,))
            return cur.fetchone()

        except con.Error as e:
            print(e.pgerror)
            return False
        finally:
            if con is not None:
                cur.close()
                con.close()


    def gestionarComite(self, opcion, idministerio, idlider, idsuplente, descripcion, observacion, creadoporusuario):

        procedimiento = 'CALL membresia.gestionar_comite(%s, %s, %s, %s, %s, %s, %s)'
        datos = (opcion, idministerio, idlider, idsuplente, descripcion, observacion, creadoporusuario,)
    
        try:
            
            consulta = Conexion()
            con = consulta.getConexion()
            cur = con.cursor()
            cur.execute(procedimiento, datos)
            con.commit()
            return True

        except con.Error as e:
            print(e.pgerror)
            return e.pgcode
        finally:
            if con is not None:
                cur.close()
                con.close()


    def traerMiembrosPerfil(self):
        funcion = 'membresia.get_miembros_perfil'
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.callproc(funcion)
            return cur.fetchone()[0]            
        except con.Error as e:
            print(e.pgerror)
            return False
        finally:
            if con is not None:
                cur.close()
                con.close()
