from app.Conexion.Conexion import Conexion

class Login_dao(Conexion):

    def __init__(self):
        Conexion.__init__(self)

    def getMenuData(self, id, gru_id):
        lista = []
        querySQL = '''SELECT us.usu_id, us.usu_nick, us.fun_id, us.gru_id, gr.gru_des
            , mo.mod_id, mo.mod_des, pag.pag_id, pag.pag_nombre, pag.pag_direcc
            , per.leer, per.insertar, per.editar, per.borrar
        FROM seguridad.usuarios us
        LEFT JOIN seguridad.grupos gr ON gr.gru_id = us.gru_id
        INNER JOIN seguridad.permisos per ON per.gru_id = gr.gru_id
        LEFT JOIN seguridad.paginas pag ON pag.pag_id = per.pag_id
        LEFT JOIN seguridad.modulos mo ON mo.mod_id = pag.mod_id 
        WHERE us.usu_id=%s AND us.gru_id=%s
        '''
        conexion = Conexion()
        conn = conexion.getConexion()
        cur = conn.cursor()
        try:
            cur.execute(querySQL, (id, gru_id,))
            data = cur.fetchall()
            if len(data) > 0:
                for rs in data:
                    obj = {}
                    obj['usu_id'] = rs[0]
                    obj['usu_nick'] = rs[1]
                    obj['fun_id'] = rs[2]
                    obj['gru_id'] = rs[3]
                    obj['gru_des'] = rs[4]
                    obj['mod_id'] = rs[5]
                    obj['mod_des'] = rs[6]
                    obj['pag_id'] = rs[7]
                    obj['pag_nombre'] = rs[8]
                    obj['pag_direcc'] = rs[9]
                    obj['leer'] = rs[10]
                    obj['insertar'] = rs[11]
                    obj['editar'] = rs[12]
                    obj['borrar'] = rs[13]
                    lista.append(obj)
        except conn.Error as e:
            print(e)
            obj = {}
            obj['codigo'] = e.pgcode
            obj['mensaje'] = e.pgerror            
        finally:
            if conn is not None:
                cur.close()
                conn.close()
        return lista

    def getSessionData(self, id):
        obj = {}
        querySQL = '''SELECT ses_id, ses_des, ses_nro_intentos, ses_duracion, ses_estado, ses_duracion_bloqueo
        FROM seguridad.sesion WHERE ses_id=%s AND ses_estado IS true;
        '''
        try:
            conn = self.getConexion()
            cur = conn.cursor()
            cur.execute(querySQL, (id,))
            data = cur.fetchall()
            if len(data) > 0:
                for rs in data:
                    obj['ses_id'] = rs[0]
                    obj['ses_des'] = rs[1]
                    obj['ses_nro_intentos'] = rs[2]
                    obj['ses_duracion'] = rs[3]
                    obj['ses_estado'] = rs[4]
                    obj['ses_duracion_bloqueo'] = rs[5]
        except conn.Error as e:
            obj['codigo'] = e.pgcode
            obj['mensaje'] = e.pgerror            
        finally:
            if conn is not None:
                cur.close()
                conn.close()
        return obj

    def searchByUser(self, user):
        obj = {}
        querySQL = '''
        SELECT u.usu_id, TRIM(u.usu_nick), u.usu_clave, u.usu_nro_intentos, u.usu_vaca_fechainicio, u.usu_vaca_fechafin, u.usu_isonline, u.usu_nro_login_exitoso
        , u.fun_id, u.gru_id, u.usu_estado, fecha_formatolargo(CURRENT_DATE)fechahoy, u.usu_imagen
        , CONCAT(p.per_nombres, ' ', p.per_apellidos)nombre_persona, g.gru_des grupo
        FROM seguridad.usuarios u
        left join referenciales.personas p on p.per_id = u.fun_id 
        left join seguridad.grupos g ON g.gru_id = u.gru_id
        WHERE u.usu_nick=%s AND u.usu_estado IS true'''
        conexion = Conexion()
        conn = conexion.getConexion()
        cur = conn.cursor()
        try:
            cur.execute(querySQL, (user,))
            data = cur.fetchall()
            if len(data) > 0:
                for rs in data:
                    obj['usu_id'] = rs[0]
                    obj['usu_nick'] = rs[1]
                    obj['usu_clave'] = rs[2]
                    obj['usu_nro_intentos'] = rs[3]
                    obj['usu_vaca_fechainicio'] = rs[4]
                    obj['usu_vaca_fechafin'] = rs[5]
                    obj['usu_isonline'] = rs[6]
                    obj['usu_nro_login_exitoso'] = rs[7]
                    obj['fun_id'] = rs[8]
                    obj['gru_id'] = rs[9]
                    obj['usu_estado'] = rs[10]
                    obj['fechahoy'] = rs[11]
                    obj['usu_imagen'] = rs[12]
                    obj['nombre_persona'] = rs[13]
                    obj['grupo'] = rs[14]
        except conn.Error as e:
            obj['codigo'] = e.pgcode
            obj['mensaje'] = e.pgerror            
        finally:
            if conn is not None:
                cur.close()
                conn.close()
        return obj

    def registerLogUser(self, obj):
        res = {}
        insertSQL = '''INSERT INTO seguridad.sesion_data_log_usuario
        (ses_id, sdlu_nick, sdlu_clave, sdlu_latitud, sdlu_longitud, sdlu_navegador, sdlu_ip, sdlu_macaddress, sdlu_fin_sesion, sdlu_estado, creacion_fecha, creacion_usuario)
        VALUES(1, %s, %s, %s, %s, %s, %s, %s, %s, %s, now(), %s)'''
        conexion = Conexion()
        conn = conexion.getConexion()
        cur = conn.cursor()
        try:
            cur.execute(insertSQL, (obj['sdlu_nick'], obj['sdlu_clave'], obj['sdlu_latitud'], obj['sdlu_longitud'], obj['sdlu_navegador']
            , obj['sdlu_ip'], obj['sdlu_macaddress'], obj['sdlu_fin_sesion'], obj['sdlu_estado'], obj['creacion_usuario'],))
            conn.commit()
            return {'exitoso':cur.fetchone()[0]}
        except conn.Error as e:
            res['codigo'] = e.pgcode
            res['mensaje'] = e.pgerror            
            return res
        finally:
            if conn is not None:
                cur.close()
                conn.close()

    def updateStatusUser(self, usu_isonline, usu_id):
        res = {}
        updateSQL = ''
        if usu_isonline:
            updateSQL = '''UPDATE seguridad.usuarios SET usu_isonline=%s, usu_nro_login_exitoso=((SELECT usu_nro_login_exitoso FROM seguridad.usuarios WHERE usu_id=%s) + 1)
            , modificacion_fecha = now(), modificacion_usuario = %s WHERE usu_id=%s'''
        else:
            updateSQL = '''UPDATE seguridad.usuarios SET usu_isonline=%s, modificacion_fecha = now(), modificacion_usuario = %s WHERE usu_id=%s'''

        conexion = Conexion()
        conn = conexion.getConexion()
        cur = conn.cursor()
        try:
            if usu_isonline:
                cur.execute(updateSQL, (usu_isonline, usu_id, usu_id, usu_id,))
            else:
                cur.execute(updateSQL, (usu_isonline, usu_id, usu_id,))
            conn.commit()
            return {'exitoso':cur.fetchone()[0]}
        except conn.Error as e:
            res['codigo'] = e.pgcode
            res['mensaje'] = e.pgerror            
            return res
        finally:
            if conn is not None:
                cur.close()
                conn.close()

    def updateIntentosErroneosUser(self, usu_id):
        res = {}
        updateSQL = '''UPDATE seguridad.usuarios SET usu_nro_intentos=((SELECT usu_nro_intentos FROM seguridad.usuarios WHERE usu_id=%s) + 1)
        , modificacion_fecha = now(), modificacion_usuario = %s WHERE usu_id=%s'''
        conexion = Conexion()
        conn = conexion.getConexion()
        cur = conn.cursor()
        try:
            cur.execute(updateSQL, (usu_id, usu_id, usu_id,))
            conn.commit()
            return {'exitoso':cur.fetchone()[0]}
        except conn.Error as e:
            res['codigo'] = e.pgcode
            res['mensaje'] = e.pgerror
            return res
        finally:
            if conn is not None:
                cur.close()
                conn.close()

    def banUser(self, usu_id, estado):
        res = {}
        updateSQL = '''UPDATE seguridad.usuarios SET usu_estado=%s
        , modificacion_fecha = now(), modificacion_usuario = %s WHERE usu_id=%s'''
        conexion = Conexion()
        conn = conexion.getConexion()
        cur = conn.cursor()
        try:
            cur.execute(updateSQL, (estado, usu_id, usu_id,))
            conn.commit()
            return {'exitoso':cur.fetchone()[0]}
        except conn.Error as e:
            res['codigo'] = e.pgcode
            res['mensaje'] = e.pgerror
            return res
        finally:
            if conn is not None:
                cur.close()
                conn.close()