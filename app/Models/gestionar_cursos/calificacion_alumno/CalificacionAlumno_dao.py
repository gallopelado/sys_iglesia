from flask import current_app as app
from app.Conexion.Conexion import Conexion

class CalificacionAlumno_dao:

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
        querySQL = '''select di.malla_id, di.cur_id, c.cur_des, di.asi_id, di.num_id, concat(a.asi_des,' ', na.num_des)asignatura, di.turno, di.per_id, CONCAT(p.per_nombres, ' ', p.per_apellidos, ' - ', p.per_ci)alumno, di.estado, CASE ( SELECT count(*) FROM cursos.calificacion_alumno ca left join cursos.planificacion_examen pe on pe.planex_id = ca.planex_id left join referenciales.personas p on p.per_id = ca.alumno_id WHERE pe.malla_id=di.malla_id AND pe.cur_id=di.cur_id AND pe.asi_id=di.asi_id AND pe.num_id=di.num_id AND pe.turno=di.turno AND ca.alumno_id = di.per_id ) WHEN 1 THEN 'CALIFICADO' WHEN 0 THEN 'SIN-CALIFICAR'  ELSE 'MAS DE UN EXAMEN CALIF.' END "isCalificado" from cursos.detalle_inscripcion di left join referenciales.personas p on p.per_id = di.per_id left join referenciales.cursos c on c.cur_id = di.cur_id left join referenciales.asignaturas a on a.asi_id = di.asi_id left join referenciales.numero_asignatura na on na.num_id = di.num_id where di.estado = 'INSCRIPTO' and di.malla_id = %s and di.cur_id = %s and di.asi_id = %s and di.num_id = %s and turno = %s'''
        conexion = Conexion()
        conn = conexion.getConexion()
        cur = conn.cursor()
        try:
            cur.execute(querySQL, (malla_id, cur_id, asi_id, num_id, turno,))
            data = cur.fetchall()
            if len(data) > 0:
                for rs in data:
                    obj = {}
                    obj['malla_id'] = rs[0]
                    obj['cur_id'] = rs[1]
                    obj['cur_des'] = rs[2]
                    obj['asi_id'] = rs[3]
                    obj['num_id'] = rs[4]
                    obj['asignatura'] = rs[5]
                    obj['turno'] = rs[6]
                    obj['per_id'] = rs[7]
                    obj['alumno'] = rs[8]
                    obj['estado'] = rs[9]
                    obj['isCalificado'] = rs[10]
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

    def getListaJustificativosByAlumno(self, alumno_id):
        lista=[]
        querySQL = '''select aj.alj_id, aj.alumno_id, aj.malla_id, aj.cur_id, aj.asi_id, asi.asi_des, aj.num_id, na.num_des, aj.alj_descripcion, fecha_formatolargo(aj.creacion_fecha::DATE)fechacreacion, aj.turno from cursos.alumno_justificativo aj left join referenciales.personas p on p.per_id = aj.per_id left join referenciales.asignaturas asi on asi.asi_id = aj.asi_id left join referenciales.numero_asignatura na on na.num_id = aj.num_id where aj.alumno_id = %s'''
        conexion = Conexion()
        conn = conexion.getConexion()
        cur = conn.cursor()
        try:
            cur.execute(querySQL, (alumno_id,))
            data = cur.fetchall()
            if len(data) > 0:
                for rs in data:
                    obj = {}
                    obj['alj_id'] = rs[0]
                    obj['alumno_id'] = rs[1]
                    obj['malla_id'] = rs[2]
                    obj['cur_id'] = rs[3]
                    obj['asi_id'] = rs[4]
                    obj['asi_des'] = rs[5]
                    obj['num_id'] = rs[6]
                    obj['num_des'] = rs[7]
                    obj['alj_descripcion'] = rs[8]
                    obj['fechacreacion'] = rs[9]
                    obj['turno'] = rs[10]
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

    def guardar(self, planex_id, alumno_id, cal_puntaje, creacion_usuario):
        obj=[]
        insertSQL = '''INSERT INTO cursos.calificacion_alumno (planex_id, alumno_id, cal_puntaje, cal_estado, creacion_fecha, creacion_usuario) VALUES(%s, %s, %s, true, now(), %s) ON CONFLICT(planex_id, alumno_id) DO UPDATE SET cal_puntaje=EXCLUDED.cal_puntaje, modificacion_fecha=now(), modificacion_usuario=EXCLUDED.creacion_usuario'''
        conexion = Conexion()
        conn = conexion.getConexion()
        cur = conn.cursor()
        try:
            cur.execute(insertSQL, (planex_id, alumno_id, cal_puntaje, creacion_usuario,))
            conn.commit()
            res = True if cur.statusmessage == 'INSERT 0 1' else False
            return res
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