from flask import current_app as app
from app.Conexion.Conexion import Conexion

class Funcionario_dao:

    def getLista(self):
        lista=[]
        querySQL = '''select fun.fun_id, CONCAT(p.per_nombres,' ', p.per_apellidos)funcionario, fun.car_id, c.car_des cargo, case fun.fun_estado when true then 'NO' else 'SI' end estado from seguridad.funcionarios fun left join referenciales.personas p on p.per_id = fun.fun_id left join seguridad.cargos c on c.car_id = fun.car_id'''
        conexion = Conexion()
        conn = conexion.getConexion()
        cur = conn.cursor()
        try:
            cur.execute(querySQL, )
            data = cur.fetchall()
            if len(data) > 0:
                for rs in data:
                    obj = {}
                    obj['fun_id'] = rs[0]
                    obj['funcionario'] = rs[1]
                    obj['idcargo'] = rs[2]
                    obj['cargo'] = rs[3]
                    obj['estado'] = rs[4]
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

    def getCargos(self):
        lista=[]
        querySQL = '''SELECT car_id, car_des FROM seguridad.cargos'''
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

    def getPersonas(self, op):
        lista = []
        if op == 1:
            querySQL = '''SELECT per_id, per_ci, CONCAT(per_nombres, ' ', per_apellidos)persona FROM referenciales.personas WHERE per_razonbaja IS null order by persona'''
        else:
            querySQL = '''SELECT per_id, per_ci, CONCAT(per_nombres, ' ', per_apellidos)persona FROM referenciales.personas WHERE per_id not in(select fun_id from seguridad.funcionarios) and per_razonbaja IS null order by persona'''
        conexion = Conexion()
        conn = conexion.getConexion()
        cur = conn.cursor()
        try:
            cur.execute(querySQL)
            data = cur.fetchall()
            if len(data) > 0:
                for rs in data:
                    obj = {}
                    obj['per_id'] = rs[0]
                    obj['per_ci'] = rs[1]
                    obj['persona'] = rs[2]
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

    def getFuncionarioId(self, id):
        obj = {}
        querySQL = '''SELECT fun.fun_id, CONCAT(p.per_ci, ' - ', p.per_nombres,' ', p.per_apellidos)funcionario, fun.car_id, fun.fun_estado FROM seguridad.funcionarios fun left join referenciales.personas p on p.per_id = fun.fun_id WHERE fun.fun_id=%s'''
        conexion = Conexion()
        conn = conexion.getConexion()
        cur = conn.cursor()
        try:
            cur.execute(querySQL, (id, ))
            rs = cur.fetchone()
            if len(rs) > 0:                
                    obj['fun_id'] = rs[0]
                    obj['funcionario'] = rs[1]
                    obj['car_id'] = rs[2]
                    obj['fun_estado'] = rs[3]
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

    def guardar(self, fun_id, car_id, usu_id):
        obj=[]
        insertSQL = '''INSERT INTO seguridad.funcionarios(fun_id, car_id, creacion_fecha, creacion_usuario)VALUES(%s, %s, now(), %s)'''
        conexion = Conexion()
        conn = conexion.getConexion()
        cur = conn.cursor()
        try:
            cur.execute(insertSQL, (fun_id, car_id, usu_id,))
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

    def modificar(self, id, car_id,usu_id):
        obj=[]
        updateSQL = '''UPDATE seguridad.funcionarios
        SET car_id=%s, modificacion_fecha=now(), modificacion_usuario=%s WHERE fun_id=%s'''
        conexion = Conexion()
        conn = conexion.getConexion()
        cur = conn.cursor()
        try:
            cur.execute(updateSQL, (car_id, usu_id, id,))
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

    def eliminar(self, id, usu_id):
        obj=[]
        deleteSQL = '''UPDATE seguridad.funcionarios SET fun_estado=false, modificacion_fecha=now(), modificacion_usuario=%s WHERE fun_id=%s'''
        conexion = Conexion()
        conn = conexion.getConexion()
        cur = conn.cursor()
        try:
            cur.execute(deleteSQL, (usu_id, id,))
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