from flask import current_app as app
from app.Conexion.Conexion import Conexion

class Pagina_dao:

    def getLista(self):
        lista=[]
        querySQL = '''SELECT pag_id, mod_id, mod_des, pag_nombre, pag_direcc, CASE pag_estado WHEN true THEN 'ACTIVO' ELSE 'INACTIVO' END FROM seguridad.paginas left join seguridad.modulos using(mod_id)'''
        conexion = Conexion()
        conn = conexion.getConexion()
        cur = conn.cursor()
        try:
            cur.execute(querySQL, )
            data = cur.fetchall()
            if len(data) > 0:
                for rs in data:
                    obj = {}
                    obj['pag_id'] = rs[0]
                    obj['mod_id'] = rs[1]
                    obj['mod_des'] = rs[2]
                    obj['pag_nombre'] = rs[3]
                    obj['pag_direcc'] = rs[4]
                    obj['pag_estado'] = rs[5]
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

    def getModulos(self):
        lista=[]
        querySQL = '''SELECT mod_id, mod_des FROM seguridad.modulos'''
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

    def getPaginaId(self, id):
        obj = {}
        querySQL = '''SELECT pag_id, mod_id, mod_des, pag_nombre, pag_direcc, pag_estado FROM seguridad.paginas left join seguridad.modulos using(mod_id) WHERE pag_id=%s'''
        conexion = Conexion()
        conn = conexion.getConexion()
        cur = conn.cursor()
        try:
            cur.execute(querySQL, (id, ))
            rs = cur.fetchone()
            if len(rs) > 0:                
                    obj['pag_id'] = rs[0]
                    obj['mod_id'] = rs[1]
                    obj['mod_des'] = rs[2]
                    obj['pag_nombre'] = rs[3]
                    obj['pag_direcc'] = rs[4]
                    obj['pag_estado'] = rs[4]
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

    def guardar(self, mod_id, pag_nombre, pag_direcc):
        obj=[]
        insertSQL = '''INSERT INTO seguridad.paginas (mod_id, pag_nombre, pag_direcc, pag_estado) VALUES(%s, %s, %s, true);'''
        conexion = Conexion()
        conn = conexion.getConexion()
        cur = conn.cursor()
        try:
            cur.execute(insertSQL, (mod_id, pag_nombre, pag_direcc,))
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

    def modificar(self, pag_nombre, mod_id, pag_direcc, pag_id):
        obj=[]
        updateSQL = '''UPDATE seguridad.paginas SET pag_nombre=%s, mod_id=%s, pag_direcc=%s WHERE pag_id=%s'''''
        conexion = Conexion()
        conn = conexion.getConexion()
        cur = conn.cursor()
        try:
            cur.execute(updateSQL, (pag_nombre, mod_id, pag_direcc, pag_id,))
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

    def eliminar(self, id):
        obj=[]
        deleteSQL = '''UPDATE seguridad.paginas SET pag_estado=FALSE WHERE pag_id=%s'''
        conexion = Conexion()
        conn = conexion.getConexion()
        cur = conn.cursor()
        try:
            cur.execute(deleteSQL, (id,))
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