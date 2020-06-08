from app.Conexion.Conexion import Conexion

class InscripcionAlumno_dao(Conexion):

    def __init__(self):
        Conexion.__init__(self)

    def getCursosPlanificados(self):
        res = {}
        lista = []
        querySQL = '''
        SELECT
            pa.malla_id, pa.estado, pa.cur_id, cu.cur_des curso
        FROM
            cursos.planificacion_aca pa
        LEFT JOIN referenciales.cursos cu ON cu.cur_id = pa.cur_id 
        LEFT JOIN cursos.malla_curricular ma ON ma.malla_id = pa.malla_id 
        LEFT JOIN referenciales.anho_habil anh ON anh.anho_id = ma.anho_id 
        WHERE anh.is_active'''
        try:
            conn = self.getConexion()
            cur = conn.cursor()
            cur.execute(querySQL)
            data = cur.fetchall()
            if len(data) > 0:
                for rs in data:
                    obj = {}
                    obj['malla_id'] = rs[0]
                    obj['estado'] = rs[1]
                    obj['cur_id'] = rs[2]
                    obj['curso'] = rs[3]
                    lista.append(obj)                    
            
        except conn.Error as e:
            res['codigo'] = e.pgcode
            res['mensaje'] = e.pgerror            
            return res
        finally:
            if conn is not None:
                cur.close()
                conn.close()
        return lista  

    def getPersonas(self):
        res = {}
        lista = []
        querySQL = '''
        SELECT per_id, per_ci, per_nombres, per_apellidos, tipoper_id, per_obs, per_fechabaja, per_razonbaja, per_fechareincorporacion, is_propietario
        FROM referenciales.personas WHERE per_fechabaja IS NULL
        '''
        try:
            conn = self.getConexion()
            cur = conn.cursor()
            cur.execute(querySQL)
            data = cur.fetchall()
            if len(data) > 0:
                for rs in data:
                    obj = {}
                    obj['per_id'] = rs[0]                    
                    obj['per_nombres'] = rs[2]
                    obj['per_apellidos'] = rs[3] 
                    obj['per_ci'] = rs[1]                   
                    lista.append(obj)                    
            
        except conn.Error as e:
            res['codigo'] = e.pgcode
            res['mensaje'] = e.pgerror            
            return res
        finally:
            if conn is not None:
                cur.close()
                conn.close()
        return lista

    def getListaAlumnosRegistradosInscripcion(self, malla_id, curso_id):
        res = {}
        lista = []
        querySQL = '''
        SELECT malla_id, cur_id, per_id, per_nombres, per_apellidos, estado
        FROM cursos.inscripcion_curso 
        LEFT JOIN referenciales.personas using(per_id)
        WHERE malla_id = %s AND cur_id = %s
        '''
        try:
            conn = self.getConexion()
            cur = conn.cursor()
            cur.execute(querySQL, (malla_id, curso_id,))
            data = cur.fetchall()
            if len(data) > 0:
                for rs in data:
                    obj = {}
                    obj['malla_id'] = rs[0]                    
                    obj['cur_id'] = rs[1]
                    obj['per_id'] = rs[2] 
                    obj['per_nombres'] = rs[3]  
                    obj['per_apellidos'] = rs[4] 
                    obj['estado'] = rs[5]                  
                    lista.append(obj)                    
            
        except conn.Error as e:
            res['codigo'] = e.pgcode
            res['mensaje'] = e.pgerror            
            return res
        finally:
            if conn is not None:
                cur.close()
                conn.close()
        return lista           

    def getListaAlumnosRegistrados(self, malla_id, curso_id):
        res = {}
        lista = []
        querySQL = '''
        SELECT
            malla_id,
            cur_id,
            per_id, per_nombres, per_apellidos,
            asi_id,
            num_id,
            turno,
            estado,
            creacion_fecha,
            creacion_usuario,
            modificacion_fecha,
            modificacion_usuario
        FROM
            cursos.detalle_inscripcion
        LEFT JOIN referenciales.personas using(per_id)
        WHERE malla_id = %s AND cur_id = %s
        '''
        try:
            conn = self.getConexion()
            cur = conn.cursor()
            cur.execute(querySQL, (malla_id, curso_id,))
            data = cur.fetchall()
            if len(data) > 0:
                for rs in data:
                    obj = {}
                    obj['malla_id'] = rs[0]                    
                    obj['cur_id'] = rs[1]
                    obj['per_id'] = rs[2] 
                    obj['per_nombres'] = rs[3]  
                    obj['per_apellidos'] = rs[4] 
                    obj['asi_id'] = rs[5] 
                    obj['num_id'] = rs[6] 
                    obj['turno'] = rs[7] 
                    obj['estado'] = rs[8]                  
                    lista.append(obj)                    
            
        except conn.Error as e:
            res['codigo'] = e.pgcode
            res['mensaje'] = e.pgerror            
            return res
        finally:
            if conn is not None:
                cur.close()
                conn.close()
        return lista

    def insertarAlumno(self, alumno):
        res = {}
        insertSQL = '''
        INSERT INTO cursos.inscripcion_curso
        (malla_id, cur_id, per_id, estado, creacion_fecha, creacion_usuario)
        VALUES(%s, %s, %s, true, now(), NULL);
        '''
        try:
            conn = self.getConexion()
            cur = conn.cursor()
            cur.execute(insertSQL, (alumno['malla_id'], alumno['curso_id'], alumno['per_id'],))
            conn.commit()
            return {'nrofilas':cur.rowcount}
        except conn.Error as e:
            res['codigo'] = e.pgcode
            res['mensaje'] = e.pgerror            
            return res
        finally:
            if conn is not None:
                cur.close()
                conn.close()