from app.Conexion.Conexion import Conexion
class PlanificacionCurso_dao(Conexion):
    def __init__(self):
        Conexion.__init__(self)

    def getMaestros(self):
        lista_maestros = []
        querySQL = '''SELECT per_id,per_nombres, per_apellidos 
        FROM referenciales.maestros m 
        LEFT JOIN referenciales.personas USING(per_id)'''
        try:
            conn = self.getConexion()
            cur = conn.cursor()
            cur.execute(querySQL)
            data = cur.fetchall()
            for item in data:
                objeto = {}
                objeto['per_id'] = item[0]
                objeto['per_nombres'] = item[1]
                objeto['per_apellidos'] = item[2]
                lista_maestros.append(objeto)

        except conn.Error as e:
            print(e.pgerror)
        finally:
            if conn is not None:
                cur.close()
                conn.close()
        return lista_maestros

    def getDetalleAsignaturas(self, idplan, idcurso):
        lista_detalle = []
        querySQL = '''
        SELECT 
            dt.malla_id,
            dt.asi_id, asi.asi_des,
            dt.num_id, nas.num_des, 
            dt.per_id idmaestro, pe.per_nombres, pe.per_apellidos,
            dt.fechainicio,
            dt.fechafin,
            dt.estado,
            dt.turno,
            dt.cur_id, cu.cur_des
        FROM 
            cursos.detalle_planificacion dt
        LEFT JOIN referenciales.cursos cu ON cu.cur_id = dt.cur_id 
        LEFT JOIN referenciales.asignaturas asi ON asi.asi_id = dt.asi_id 
        LEFT JOIN referenciales.asignatura_tomo asit ON asit.asi_id = asi.asi_id AND asit.num_id = dt.num_id 
        LEFT JOIN referenciales.numero_asignatura nas ON nas.num_id = asit.num_id 
        LEFT JOIN referenciales.personas pe ON pe.per_id = dt.per_id
        WHERE dt.malla_id = %s AND dt.cur_id = %s
        ORDER BY nas.num_des
        '''
        try:
            conn = self.getConexion()
            cur = conn.cursor()
            cur.execute(querySQL, (idplan, idcurso,))
            data = cur.fetchall()
            for item in data:
                objeto = {}
                objeto['malla_id'] = item[0]
                objeto['asi_id'] = item[1]
                objeto['asi_des'] = item[2]
                objeto['num_id'] = item[3]
                objeto['num_des'] = item[4]
                objeto['idmaestro'] = item[5]
                objeto['per_nombres'] = item[6]
                objeto['per_apellidos'] = item[7]
                objeto['fechainicio'] = item[8]
                objeto['fechafin'] = item[9]
                objeto['estado'] = item[10]
                objeto['turno'] = item[11]
                objeto['cur_id'] = item[12]
                objeto['cur_des'] = item[13]                
                lista_detalle.append(objeto)

        except conn.Error as e:
            print(e.pgerror)
        finally:
            if conn is not None:
                cur.close()
                conn.close()
        return lista_detalle