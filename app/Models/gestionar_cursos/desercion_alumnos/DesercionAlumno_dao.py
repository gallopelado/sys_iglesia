from app.Conexion.Conexion import Conexion

class DesercionAlumno_dao(Conexion):

    def __init__(self):
        Conexion.__init__(self)

    def getMaestros(self):
        res = {}
        lista = []
        querySQL = '''
        SELECT
            DISTINCT(dp.per_id), CONCAT(p.per_nombres, ' ', p.per_apellidos) maestro
        FROM
            cursos.detalle_planificacion dp
        LEFT JOIN referenciales.maestros m 
            ON m.per_id =  dp.per_id 
        LEFT JOIN referenciales.personas p 
            ON p.per_id = m.per_id 
        WHERE 
            dp.estado IS TRUE
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
                    obj['maestro'] = rs[1]
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

    def getCursoMaestro(self, perid, turno):
        res = {}
        lista = []
        querySQL = '''
        SELECT
            dp.malla_id,
            dp.cur_id, c.cur_des curso,
            dp.turno,
            dp.per_id, CONCAT(p.per_nombres, ' ', p.per_apellidos) maestro,
            dp.fechainicio::VARCHAR
        FROM
            cursos.detalle_planificacion dp
        LEFT JOIN referenciales.cursos c 
            ON c.cur_id = dp.cur_id 
        LEFT JOIN referenciales.maestros m 
            ON m.per_id =  dp.per_id 
        LEFT JOIN referenciales.personas p 
            ON p.per_id = m.per_id 
        WHERE 
            dp.per_id = %s AND dp.turno = %s
        '''
        try:
            conn = self.getConexion()
            cur = conn.cursor()
            cur.execute(querySQL, (perid, turno,))
            data = cur.fetchall()
            if len(data) > 0:
                for rs in data:
                    obj = {}
                    obj['malla_id'] = rs[0]
                    obj['cur_id'] = rs[1]
                    obj['curso'] = rs[2]
                    obj['turno'] = rs[3]
                    obj['maestro'] = rs[4]
                    obj['fechainicio'] = rs[5]
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
            return {'exitoso':cur.fetchone()}
        except conn.Error as e:
            res['codigo'] = e.pgcode
            res['mensaje'] = e.pgerror            
            return res
        finally:
            if conn is not None:
                cur.close()
                conn.close()