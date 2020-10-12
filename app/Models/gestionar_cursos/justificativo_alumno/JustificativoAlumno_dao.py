from flask import current_app as app
from app.Conexion.Conexion import Conexion

class JustificativoAlumno_dao:

    def getLista(self):
        lista=[]
        querySQL = '''SELECT dp.malla_id, dp.cur_id, c.cur_des, dp.asi_id, a.asi_des, dp.num_id, na.num_des, dp.per_id, CONCAT(p.per_nombres, ' ', p.per_apellidos)docente, dp.fechainicio, dp.fechafin, dp.estado, dp.turno FROM cursos.detalle_planificacion dp left join referenciales.cursos c on c.cur_id = dp.cur_id left join referenciales.asignaturas a on a.asi_id = dp.asi_id left join referenciales.numero_asignatura na on na.num_id = dp.num_id left join referenciales.personas p on p.per_id = dp.per_id'''
        conexion = Conexion()
        conn = conexion.getConexion()
        cur = conn.cursor()
        try:
            cur.execute(querySQL, )
            data = cur.fetchall()
            if len(data) > 0:
                for rs in data:
                    obj = {}
                    obj['malla_id'] = rs[0]
                    obj['cur_id'] = rs[1]
                    obj['cur_des'] = rs[2]
                    obj['asi_id'] = rs[3]
                    obj['asi_des'] = rs[4]
                    obj['num_id'] = rs[5]
                    obj['num_des'] = rs[6]
                    obj['per_id'] = rs[7]
                    obj['docente'] = rs[8]
                    obj['fechainicio'] = rs[9]
                    obj['fechafin'] = rs[10]
                    obj['estado'] = rs[11]
                    obj['turno'] = rs[12]
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

    def getListaAlumnos(self, malla_id, cur_id, asi_id, num_id, turno):
        lista=[]
        querySQL = '''SELECT adt.asiscurso_id, adt.per_id, CONCAT(p.per_nombres,' ', p.per_apellidos)estudiante , ac.malla_id, ac.cur_id, c.cur_des, ac.asi_id, ac.num_id, CONCAT(asi.asi_des,' ', na.num_des)asignatura, ac.turno , ac.per_id idmaestro, CONCAT(p2.per_nombres,' ', p2.per_apellidos)maestro FROM cursos.asistenciacurso_det adt LEFT JOIN referenciales.personas p ON p.per_id = adt.per_id LEFT JOIN cursos.asistenciacurso_cab ac ON ac.asiscurso_id = adt.asiscurso_id LEFT JOIN referenciales.cursos c ON c.cur_id = ac.cur_id LEFT JOIN referenciales.asignaturas asi ON asi.asi_id = ac.asi_id LEFT JOIN referenciales.numero_asignatura na ON na.num_id = ac.num_id LEFT JOIN referenciales.personas p2 ON p2.per_id = ac.per_id WHERE adt.asiscursodet_asistio IS FALSE AND ac.malla_id = %s AND ac.cur_id = %s AND ac.asi_id = %s AND ac.num_id = %s AND ac.turno = %s'''
        conexion = Conexion()
        conn = conexion.getConexion()
        cur = conn.cursor()
        try:
            cur.execute(querySQL, (malla_id, cur_id, asi_id, num_id, turno,))
            data = cur.fetchall()
            if len(data) > 0:
                for rs in data:
                    obj = {}
                    obj['asiscurso_id'] = rs[0]
                    obj['per_id'] = rs[1]
                    obj['estudiante'] = rs[2]
                    obj['malla_id'] = rs[3]
                    obj['cur_id'] = rs[4]
                    obj['cur_des'] = rs[5]
                    obj['asi_id'] = rs[6]
                    obj['num_id'] = rs[7]
                    obj['asignatura'] = rs[8]
                    obj['turno'] = rs[9]
                    obj['idmaestro'] = rs[10]
                    obj['maestro'] = rs[11]
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

    def guardar(self, alumno_id, malla_id, cur_id, asi_id, num_id, per_id, turno, alj_descripcion, creacion_usuario):
        obj=[]
        insertSQL = '''INSERT INTO cursos.alumno_justificativo (alumno_id, malla_id, cur_id, asi_id, num_id, per_id, turno, alj_descripcion, alj_estado, creacion_fecha, creacion_usuario) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, true, now(), %s)RETURNING alj_id'''
        conexion = Conexion()
        conn = conexion.getConexion()
        cur = conn.cursor()
        try:
            cur.execute(insertSQL, (alumno_id, malla_id, cur_id, asi_id, num_id, per_id, turno, alj_descripcion, creacion_usuario,))
            conn.commit()
            return cur.fetchone()[0]
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