from flask import current_app as app
from jinja2.runtime import identity
from app.Conexion.Conexion import Conexion

class Permiso_dao:

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

    def getGruposId(self, id):
        obj = {}
        querySQL = '''SELECT gru_id, gru_des FROM seguridad.grupos WHERE gru_id=%s'''
        conexion = Conexion()
        conn = conexion.getConexion()
        cur = conn.cursor()
        try:
            cur.execute(querySQL, (id,))
            rs = cur.fetchone()
            obj['id'] = rs[0]
            obj['descripcion'] = rs[1]
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

    def getPaginaByModulo(self, mod_id, gru_id):
        lista=[]
        #querySQL = '''SELECT pag_id, pag_nombre FROM seguridad.paginas left join seguridad.modulos using(mod_id) where mod_id = %s'''
        querySQL = '''SELECT pag_id, pag_nombre FROM seguridad.paginas left join seguridad.modulos using(mod_id) where mod_id = %s and pag_id not in (select pag_id from seguridad.permisos where gru_id = %s)'''
        conexion = Conexion()
        conn = conexion.getConexion()
        cur = conn.cursor()
        try:
            cur.execute(querySQL, (mod_id, gru_id,))
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

    def getPaginasByGrupo(self, gru_id):
        lista=[]
        querySQL = '''SELECT pag_id, pag_nombre,gru_id, gru_des , case leer when true then 'SI' else 'NO' end leer , case insertar when true then'SI' else 'NO' end insertar , case editar when true then 'SI' else 'NO' end editar , case borrar when true then 'SI' else 'NO' end borrar FROM seguridad.permisos left join seguridad.grupos using(gru_id) left join seguridad.paginas using(pag_id) where gru_id = %s'''
        conexion = Conexion()
        conn = conexion.getConexion()
        cur = conn.cursor()
        try:
            cur.execute(querySQL, (gru_id,))
            data = cur.fetchall()
            if len(data) > 0:
                for rs in data:
                    obj = {}
                    obj['pag_id'] = rs[0]
                    obj['pag_nombre'] = rs[1]
                    obj['gru_id'] = rs[2]
                    obj['gru_des'] = rs[3]
                    obj['leer'] = rs[4]
                    obj['insertar'] = rs[5]
                    obj['editar'] = rs[6]
                    obj['borrar'] = rs[7]
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

    def getPermisoById(self, id_pagina, id_grupo):
        obj = {}
        querySQL = '''SELECT pag_id, pag_nombre, gru_id, gru_des , leer , insertar , editar , borrar FROM seguridad.permisos left join seguridad.grupos using(gru_id) left join seguridad.paginas using(pag_id) where gru_id = %s and pag_id = %s'''
        conexion = Conexion()
        conn = conexion.getConexion()
        cur = conn.cursor()
        try:
            cur.execute(querySQL, (id_grupo, id_pagina,))
            rs = cur.fetchone()
            if len(rs) > 0:                
                    obj['pag_id'] = rs[0]
                    obj['mod_id'] = rs[1]
                    obj['mod_des'] = rs[2]
                    obj['pag_nombre'] = rs[3]
                    obj['leer'] = rs[4]
                    obj['insertar'] = rs[5]
                    obj['editar'] = rs[6]
                    obj['borrar'] = rs[7]
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

    def guardar(self, pag_id, gru_id, leer, insertar, editar, borrar):
        obj=[]
        insertSQL = '''INSERT INTO seguridad.permisos (pag_id, gru_id, leer, insertar, editar, borrar) VALUES(%s, %s, %s, %s, %s, %s) on conflict (pag_id, gru_id) do update set leer = excluded.leer, insertar = excluded.insertar, editar = excluded.editar, borrar = excluded.borrar'''
        conexion = Conexion()
        conn = conexion.getConexion()
        cur = conn.cursor()
        try:
            cur.execute(insertSQL, (pag_id, gru_id, leer, insertar, editar, borrar,))
            conn.commit()
            return True
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

    def eliminar(self, gru_id, pag_id):
        obj=[]
        deleteSQL = '''DELETE FROM seguridad.permisos WHERE gru_id=%s AND pag_id=%s'''
        conexion = Conexion()
        conn = conexion.getConexion()
        cur = conn.cursor()
        try:
            cur.execute(deleteSQL, (gru_id, pag_id,))
            conn.commit()
            return True
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