from app.Conexion.Conexion import Conexion

class AsistenciaAlumno_dao(Conexion):

    def __init__(self):
        Conexion.__init__(self)

    def getListaProfesorCursosAsignatura(self, idmalla, turno, idprofesor):
        res = {}
        lista = []
        querySQL = '''SELECT malla_id, cur_id, asi_id, num_id, per_id, cur_des, asi_des, num_des, dia, fecha::VARCHAR, fecha_formatolargo(fecha)fecha_larga 
        FROM cursos.lista_cursos_fecha(%s, %s, %s) ORDER BY fecha ASC'''
        try:
            conn = self.getConexion()
            cur = conn.cursor()
            cur.execute(querySQL, (idmalla, turno, idprofesor))
            data = cur.fetchall()
            if len(data) > 0:
                for rs in data:
                    obj = {}
                    obj['malla_id'] = rs[0]
                    obj['cur_id'] = rs[1]
                    obj['asi_id'] = rs[2]
                    obj['num_id'] = rs[3]
                    obj['per_id'] = rs[4]
                    obj['cur_des'] = rs[5]
                    obj['asi_des'] = rs[6]
                    obj['num_des'] = rs[7]
                    obj['dia'] = rs[8]
                    obj['fecha'] = rs[9]
                    obj['fecha_larga'] = rs[10]
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

    def getListaAlumnosAsignatura(self, idmalla, cur_id, asi_id, num_id, turno):
        res = {}
        lista = []
        querySQL = '''SELECT di.per_id idalumno, pe.per_nombres, pe.per_apellidos FROM cursos.detalle_inscripcion di
        LEFT JOIN referenciales.personas pe ON pe.per_id = di.per_id
        WHERE di.malla_id = %s AND di.cur_id = %s AND di.asi_id = %s AND di.num_id = %s AND di.turno = %s;
        '''
        try:
            conn = self.getConexion()
            cur = conn.cursor()
            cur.execute(querySQL, (idmalla, cur_id, asi_id, num_id, turno,))
            data = cur.fetchall()
            if len(data) > 0:
                for rs in data:
                    obj = {}
                    obj['idalumno'] = rs[0]
                    obj['per_nombres'] = rs[1]
                    obj['per_apellidos'] = rs[2]
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