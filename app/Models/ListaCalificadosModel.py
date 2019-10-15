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


    def nroAdmitidos(self, idpostulacion):

        consultaSQL = 'SELECT count(*) FROM membresia.candi_admitidos WHERE post_id = %s'

        try:

            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.execute(consultaSQL, (idpostulacion,))
            return cur.fetchone()[0]

        except con.Error as e:
            print(e.pgerror)
            return False
        finally:
            if con is not None:
                cur.close()
                con.close()

    
    def traerInfoPerfil(self, idperfil):
        '''traerInfoPerfil.

        Obtiene el perfil según id en formato json.

        '''
        consultaSQL = '''        
        SELECT 
            array_to_json(array_agg(row_to_json(consulta)))
        FROM
            (            
                SELECT mper_id idperfil, 
                mper_serviren serviren, 
                mper_cualipers cualidad_personal, 
                mper_actiminis actitud_ministerial, 
                mper_anteced antecendentes, 
                (SELECT TO_CHAR(mper_fecha, 'DD "de" TMMonth "del" YYYY')) ultimafecha, 
                mper_estado, creado_por_usuario
                FROM membresia.miembro_perfil
                WHERE mper_id = %s AND mper_estado IS NOT FALSE	
            
            ) consulta;
        '''

        try:
            
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.execute(consultaSQL, (idperfil,))
            return cur.fetchone()[0][0]

        except con.Error as e:
            print(e.pgerror)
            return False
        finally:
            if con is not None:
                cur.close()
                con.close()


    def verificaCalificados(self, idpostulacion):
        
        consultaSQL = '''
        SELECT mo_id
        FROM membresia.candi_admitidos
        WHERE post_id = %s;
         '''
        try:
            
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.execute(consultaSQL, (idpostulacion,))
            return cur.fetchall()

        except con.Error as e:
            print(e.pgerror)
            return False
        finally:
            if con is not None:
                cur.close()
                con.close()