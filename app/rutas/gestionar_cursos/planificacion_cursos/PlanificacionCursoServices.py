from app.Models.gestionar_cursos.planificacion_curso.PlanificacionCurso_dao import PlanificacionCurso_dao
class PlanificacionCursoServices:

    def __init__(self):
        self.__plan_dao = PlanificacionCurso_dao()

    def getMaestros(self):
        return self.__plan_dao.getMaestros()

    def getDetalleAsignaturas(self, idplan, idcurso):
        lista_detalle_nueva = []
        lista_obtenida = self.__plan_dao.getDetalleAsignaturas(idplan, idcurso)
        for item in lista_obtenida:
            objeto = {}
            objeto['malla_id'] = item['malla_id']
            objeto['asi_id'] = item['asi_id']
            objeto['asi_des'] = item['asi_des']
            objeto['num_id'] = item['num_id']
            objeto['num_des'] = item['num_des']
            objeto['idmaestro'] = item['idmaestro']
            objeto['per_nombres'] = item['per_nombres']
            objeto['per_apellidos'] = item['per_apellidos']
            objeto['fechainicio'] = item['fechainicio'].strftime("%x")
            objeto['fechafin'] = item['fechafin'].strftime("%x")
            objeto['estado'] = item['estado']
            objeto['turno'] = item['turno']
            objeto['cur_id'] = item['cur_id']
            objeto['cur_des'] = item['cur_des']
            lista_detalle_nueva.append(objeto)

        return lista_detalle_nueva

    def registrarCurso(self, malla_id, cur_id):
        return self.__plan_dao.registrarCurso(malla_id, cur_id)

    def registrarDetallePlan(self, malla_id, asi_id, num_id, per_id, cur_id, fechainicio, fechafin, turno):
        return self.__plan_dao.registrarDetallePlan(malla_id, asi_id, num_id, per_id, cur_id, fechainicio, fechafin, turno)

    def getDetalleFrecuencia(self, malla_id, asi_id, num_id, per_id, cur_id, turno):
        lista_detalle = []
        data = self.__plan_dao.getDetalleFrecuencia(malla_id, asi_id, num_id, per_id, cur_id, turno)        
        for item in data:
            objeto = {}
            objeto['frma_id'] = item['frma_id']
            objeto['malla_id'] = item['malla_id']
            objeto['asi_id'] = item['asi_id']
            objeto['asi_des'] = item['asi_des']
            objeto['num_id'] = item['num_id']
            objeto['num_des'] = item['num_des']
            objeto['turno'] = item['turno']
            objeto['per_id'] = item['per_id']
            objeto['frma_dia'] = item['frma_dia']
            objeto['frma_estado'] = item['frma_estado']
            objeto['cur_id'] = item['cur_id']
            objeto['frma_horainicio'] = item['frma_horainicio'].strftime("%H:%M")
            objeto['frma_horafin'] = item['frma_horafin'].strftime("%H:%M")
            lista_detalle.append(objeto)
        return lista_detalle

    def registrarDetalleFrecuencia(self, malla_id, asi_id, num_id, turno, per_id, dia, cur_id, horainicio, horafin):
        return self.__plan_dao.registrarDetalleFrecuencia(malla_id, asi_id, num_id, turno, per_id, dia, cur_id, horainicio, horafin)

    def eliminarAsignaturaFrecuencia(self, id):
        return self.__plan_dao.eliminarAsignaturaFrecuencia(id)