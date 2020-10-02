from flask import current_app as app
from app.Conexion.Conexion import Conexion

class Usuario_dao:

    def getLista(self):
        lista=[]
        querySQL = '''SELECT usu_id, usu_nick, CASE usu_isonline WHEN true THEN 'SI' ELSE 'NO' END , usu_nro_login_exitoso, fun_id, gru_id , CASE usu_estado WHEN true THEN 'NO' ELSE 'SI' END estado, modificacion_fecha FROM seguridad.usuarios'''
        conexion = Conexion()
        conn = conexion.getConexion()
        cur = conn.cursor()
        try:
            cur.execute(querySQL, )
            data = cur.fetchall()
            if len(data) > 0:
                for rs in data:
                    obj = {}
                    obj['usu_id'] = rs[0]
                    obj['usu_nick'] = rs[1]
                    obj['usu_isonline'] = rs[2]
                    obj['usu_nro_login_exitoso'] = rs[3]
                    obj['fun_id'] = rs[4]
                    obj['gru_id'] = rs[5]
                    obj['estado'] = rs[6]
                    obj['modificacion_fecha'] = rs[7]
                    lista.append(obj)
        except conn.Error as e:
            app.logger.error(e)     
            obj = {}
            obj['codigo'] = e.pgcode
            obj['mensaje'] = e.pgerror            
        finally:
            if conn is not None:
                cur.close()
                conn.close()
        return lista

    def getGrupos(self):
        lista=[]
        querySQL = '''SELECT gru_id, gru_des FROM seguridad.grupos'''
        conexion = Conexion()
        conn = conexion.getConexion()
        cur = conn.cursor()
        try:
            cur.execute(querySQL)
            data = cur.fetchall()
            if len(data) > 0:
                for rs in data:
                    obj = {}
                    obj['id'] = rs[0]
                    obj['descripcion'] = rs[1]                    
                    lista.append(obj)
        except conn.Error as e:
            app.logger.error(e)     
            obj = {}
            obj['codigo'] = e.pgcode
            obj['mensaje'] = e.pgerror
            lista.append(obj)            
        finally:
            if conn is not None:
                cur.close()
                conn.close()
        return lista

    def getFuncionarios(self):
        lista = []
        querySQL = '''SELECT fun.fun_id, CONCAT(per.per_nombres, ' ', per.per_apellidos)funcionario FROM seguridad.funcionarios fun LEFT JOIN referenciales.personas per ON per.per_id = fun.fun_id WHERE fun.fun_estado IS true AND fun.fun_id NOT IN (SELECT fun_id FROM seguridad.usuarios)'''
        conexion = Conexion()
        conn = conexion.getConexion()
        cur = conn.cursor()
        try:
            cur.execute(querySQL)
            data = cur.fetchall()
            if len(data) > 0:
                for rs in data:
                    obj = {}
                    obj['fun_id'] = rs[0]
                    obj['funcionario'] = rs[1]                    
                    lista.append(obj)
        except conn.Error as e:
            app.logger.error(e)     
            obj = {}
            obj['codigo'] = e.pgcode
            obj['mensaje'] = e.pgerror
            lista.append(obj)            
        finally:
            if conn is not None:
                cur.close()
                conn.close()
        return lista

    def getUsuarioId(self, id):
        obj = {}
        querySQL = '''SELECT u.usu_id, u.usu_nick, u.usu_clave , u.fun_id, CONCAT(p.per_nombres, ' ', p.per_apellidos) funcionario , u.gru_id, g.gru_des FROM seguridad.usuarios u LEFT JOIN seguridad.funcionarios f ON f.fun_id = u.fun_id LEFT JOIN referenciales.personas p ON p.per_id = f.fun_id LEFT JOIN seguridad.grupos g ON g.gru_id = u.gru_id WHERE u.usu_id=%s'''
        conexion = Conexion()
        conn = conexion.getConexion()
        cur = conn.cursor()
        try:
            cur.execute(querySQL, (id, ))
            rs = cur.fetchone()
            if rs:
                obj['usu_id'] = rs[0]
                obj['usu_nick'] = rs[1]
                obj['usu_clave'] = rs[2]
                obj['fun_id'] = rs[3]
                obj['funcionario'] = rs[4]
                obj['gru_id'] = rs[5]
                obj['gru_des'] = rs[6]
        except conn.Error as e:
            app.logger.error(e)
            obj = {}
            obj['codigo'] = e.pgcode
            obj['mensaje'] = e.pgerror
        finally:
            if conn is not None:
                cur.close()
                conn.close()
        return obj

    def guardar(self, usu_nick, usu_clave, fun_id, gru_id, creacion_usuario):
        obj=[]
        insertSQL = '''INSERT INTO seguridad.usuarios(usu_nick, usu_clave, fun_id, gru_id, usu_estado, creacion_fecha, creacion_usuario)VALUES(%s, %s, %s, %s, TRUE, now(), %s)'''
        conexion = Conexion()
        conn = conexion.getConexion()
        cur = conn.cursor()
        try:
            cur.execute(insertSQL, (usu_nick, usu_clave, fun_id, gru_id, creacion_usuario,))
            conn.commit()
            return cur.fetchone()
        except conn.Error as e:
            app.logger.error(e)
            obj = {}
            obj['codigo'] = e.pgcode
            obj['mensaje'] = e.pgerror
            return obj            
        finally:
            if conn is not None:
                cur.close()
                conn.close()

    def modificar(self, usu_nick, usu_clave, gru_id, modificacion_usuario, usu_id):
        obj=[]
        updateSQL = '''UPDATE seguridad.usuarios SET usu_nick=%s, usu_clave=%s, gru_id=%s, modificacion_fecha=now(), modificacion_usuario=%s WHERE usu_id=%s'''
        conexion = Conexion()
        conn = conexion.getConexion()
        cur = conn.cursor()
        try:
            cur.execute(updateSQL, (usu_nick, usu_clave, gru_id, modificacion_usuario, usu_id,))
            conn.commit()
            return cur.fetchone()
        except conn.Error as e:
            app.logger.error(e)     
            obj = {}
            obj['codigo'] = e.pgcode
            obj['mensaje'] = e.pgerror
            return obj
        finally:
            if conn is not None:
                cur.close()
                conn.close()

    def darBaja(self, usu_id, modificacion_usuario):
        obj=[]
        deleteSQL = '''UPDATE seguridad.usuarios SET usu_estado=false, modificacion_fecha=now(), modificacion_usuario=%s WHERE usu_id=%s'''
        conexion = Conexion()
        conn = conexion.getConexion()
        cur = conn.cursor()
        try:
            cur.execute(deleteSQL, (modificacion_usuario, usu_id,))
            conn.commit()
            return cur.fetchone()
        except conn.Error as e:
            app.logger.error(e)     
            obj = {}
            obj['codigo'] = e.pgcode
            obj['mensaje'] = e.pgerror
            return obj
        finally:
            if conn is not None:
                cur.close()
                conn.close()

    def resetIntentosFallidos(self, usu_id, modificacion_usuario):
        obj=[]
        updateSQL = '''UPDATE seguridad.usuarios SET usu_nro_intentos=0, modificacion_fecha=now(), modificacion_usuario=%s WHERE usu_id=%s'''
        conexion = Conexion()
        conn = conexion.getConexion()
        cur = conn.cursor()
        try:
            cur.execute(updateSQL, (modificacion_usuario, usu_id,))
            conn.commit()
            return cur.fetchone()
        except conn.Error as e:
            app.logger.error(e)     
            obj = {}
            obj['codigo'] = e.pgcode
            obj['mensaje'] = e.pgerror
            return obj
        finally:
            if conn is not None:
                cur.close()
                conn.close()

    def cambiarGrupo(self, gru_id, usu_id, modificacion_usuario):
        if self.verificaCoincidenciaGrupo(gru_id, usu_id):
            app.logger.error('Ya existe un usuario con este grupo. Verifique.')
            return False
        obj=[]
        updateSQL = '''UPDATE seguridad.usuarios SET gru_id=%s, modificacion_fecha=now(), modificacion_usuario=%s WHERE usu_id=%s'''
        conexion = Conexion()
        conn = conexion.getConexion()
        cur = conn.cursor()
        try:
            cur.execute(updateSQL, (gru_id, modificacion_usuario, usu_id,))
            conn.commit()
            return cur.fetchone()
        except conn.Error as e:
            app.logger.error(e)     
            obj = {}
            obj['codigo'] = e.pgcode
            obj['mensaje'] = e.pgerror
            return obj
        finally:
            if conn is not None:
                cur.close()
                conn.close()

    def verificaCoincidenciaGrupo(self, gru_id, usu_id):
        obj=[]
        querySQL = '''SELECT gru_id FROM seguridad.usuarios WHERE usu_id=%s AND gru_id=%s'''
        conexion = Conexion()
        conn = conexion.getConexion()
        cur = conn.cursor()
        try:
            cur.execute(querySQL, (usu_id, gru_id,))
            return True if cur.fetchone() is not None else False
        except conn.Error as e:
            app.logger.error(e)     
            obj = {}
            obj['codigo'] = e.pgcode
            obj['mensaje'] = e.pgerror
            return obj
        finally:
            if conn is not None:
                cur.close()
                conn.close()