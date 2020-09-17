from app.Conexion.Conexion import Conexion

class DesercionAlumno_dao(Conexion):

    def __init__(self):
        Conexion.__init__(self)

    def getCursosInscriptos(self):
        res = {}
        lista = []
        querySQL = '''
        SELECT DISTINCT(ic.malla_id)malla_id, ic.cur_id, c.cur_des curso
        FROM cursos.inscripcion_curso ic
        LEFT JOIN referenciales.cursos c ON c.cur_id = ic.cur_id 
        WHERE EXTRACT(YEAR FROM ic.creacion_fecha) = EXTRACT(YEAR FROM CURRENT_DATE)'''
        try:
            conn = self.getConexion()
            cur = conn.cursor()
            cur.execute(querySQL)
            data = cur.fetchall()
            if len(data) > 0:
                for rs in data:
                    obj = {}
                    obj['malla_id'] = rs[0]
                    obj['cur_id'] = rs[1]
                    obj['curso'] = rs[2]
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

    def getListaAlumnos(self, cur_id):
        res = {}
        lista = []
        querySQL = '''
        SELECT ic.malla_id, ic.cur_id, c.cur_des, ic.per_id, CONCAT(p.per_nombres, ' ', p.per_apellidos)alumno, p.per_ci cedula
        FROM cursos.inscripcion_curso ic
        LEFT JOIN referenciales.cursos c ON c.cur_id = ic.cur_id 
        LEFT JOIN referenciales.personas p ON p.per_id = ic.per_id 
        WHERE EXTRACT(YEAR FROM ic.creacion_fecha) = EXTRACT(YEAR FROM CURRENT_DATE) AND ic.cur_id=%s AND ic.estado IS TRUE'''
        try:
            conn = self.getConexion()
            cur = conn.cursor()
            cur.execute(querySQL, (cur_id,))
            data = cur.fetchall()
            if len(data) > 0:
                for rs in data:
                    obj = {}
                    obj['malla_id'] = rs[0]
                    obj['cur_id'] = rs[1]
                    obj['curso'] = rs[2]
                    obj['per_id'] = rs[3]
                    obj['alumno'] = rs[4]
                    obj['cedula'] = rs[5]
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

    def getMotivoDesercion(self):
        res = {}
        lista = []
        querySQL = 'SELECT md_id id, md_des descripcion FROM referenciales.motivo_desercion'
        try:
            conn = self.getConexion()
            cur = conn.cursor()
            cur.execute(querySQL)
            data = cur.fetchall()
            if len(data) > 0:
                for rs in data:
                    obj = {}
                    obj['id'] = rs[0]
                    obj['descripcion'] = rs[1]
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

    def registrarDesercion(self, obj):
        res = {}
        procedimiento = 'cursos.registrar_desercion'
        try:
            conn = self.getConexion()
            cur = conn.cursor()
            cur.callproc(procedimiento, (obj['mallaid'], obj['curid'], obj['perid'], obj['mdid'], obj['alddescripcion'],
            obj['aldestado'], None, None))
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