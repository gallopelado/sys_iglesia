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
