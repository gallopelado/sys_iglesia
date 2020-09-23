from flask import current_app as app
from app.Conexion.Conexion import Conexion

class MotivoDesercion_dao:

    def getLista(self):
        lista=[]
        querySQL = '''SELECT md_id id, md_des descripcion FROM referenciales.motivo_desercion'''
        conexion = Conexion()
        conn = conexion.getConexion()
        cur = conn.cursor()
        try:
            cur.execute(querySQL, )
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
        finally:
            if conn is not None:
                cur.close()
                conn.close()
        app.logger.info(lista)
        return lista

    def getMotivoId(self, id):
        obj = {}
        querySQL = '''SELECT md_id, md_des FROM referenciales.motivo_desercion WHERE md_id=%s'''
        conexion = Conexion()
        conn = conexion.getConexion()
        cur = conn.cursor()
        try:
            cur.execute(querySQL, (id, ))
            rs = cur.fetchone()
            if len(rs) > 0:                
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

    def guardar(self, descripcion, usu_id):
        obj=[]
        insertSQL = '''INSERT INTO referenciales.motivo_desercion(md_des, creacion_fecha, creacion_usuario)VALUES(%s, now(), %s)'''
        conexion = Conexion()
        conn = conexion.getConexion()
        cur = conn.cursor()
        try:
            cur.execute(insertSQL, (descripcion, usu_id,))
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

    def modificar(self, id, descripcion, usu_id):
        obj=[]
        updateSQL = '''UPDATE referenciales.motivo_desercion
        SET md_des=%s, modificacion_fecha=now(), modificacion_usuario=%s WHERE md_id=%s'''
        conexion = Conexion()
        conn = conexion.getConexion()
        cur = conn.cursor()
        try:
            cur.execute(updateSQL, (descripcion, usu_id, id,))
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
        deleteSQL = '''DELETE FROM referenciales.motivo_desercion WHERE md_id=%s'''
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