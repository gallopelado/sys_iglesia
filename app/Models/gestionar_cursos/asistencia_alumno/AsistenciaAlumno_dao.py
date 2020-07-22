from app.Conexion.Conexion import Conexion

class AsistenciaAlumno_dao(Conexion):

    def __init__(self):
        Conexion.__init__(self)

    def getListaProfesorCursosAsignatura(self, turno, idprofesor):
        res = {}
        lista = []
        querySQL = '''
        SELECT 
            dp.malla_id, dp.asi_id, a.asi_des, dp.num_id, na.num_des , dp.per_id, dp.fechainicio
            , dp.fechafin, dp.estado, dp.turno, dp.cur_id, c.cur_des
            , p.per_nombres, p.per_apellidos 
        FROM cursos.detalle_planificacion dp
        LEFT JOIN referenciales.cursos c ON c.cur_id = dp.cur_id 
        LEFT JOIN referenciales.asignaturas a ON a.asi_id = dp.asi_id 
        LEFT JOIN referenciales.numero_asignatura na ON na.num_id = dp.num_id 
        LEFT JOIN referenciales.maestros m ON m.per_id = dp.per_id 
        LEFT JOIN referenciales.personas p ON p.per_id = m.per_id 
        LEFT JOIN cursos.malla_curricular mc ON mc.malla_id = dp.malla_id 
        WHERE mc.estado IS TRUE AND dp.turno = %s AND dp.per_id = %s
        '''
        try:
            conn = self.getConexion()
            cur = conn.cursor()
            cur.execute(querySQL, (turno, idprofesor))
            data = cur.fetchall()
            if len(data) > 0:
                for rs in data:
                    obj = {}
                    obj['malla_id'] = rs[0]
                    obj['asi_id'] = rs[1]
                    obj['asi_des'] = rs[2]
                    obj['num_id'] = rs[3]
                    obj['num_des'] = rs[4]
                    obj['per_id'] = rs[5]
                    obj['fechainicio'] = rs[6]
                    obj['fechafin'] = rs[7]
                    obj['estado'] = rs[8]
                    obj['turno'] = rs[9]
                    obj['cur_id'] = rs[10]
                    obj['cur_des'] = rs[11]
                    obj['per_nombres'] = rs[12]
                    obj['per_apellidos'] = rs[13]
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