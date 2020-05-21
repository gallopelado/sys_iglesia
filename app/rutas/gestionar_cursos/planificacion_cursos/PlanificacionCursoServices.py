from app.Models.gestionar_cursos.planificacion_curso.PlanificacionCurso_dao import PlanificacionCurso_dao
class PlanificacionCursoServices:

    def __init__(self):
        self.__plan_dao = PlanificacionCurso_dao()

    def getMaestros(self):
        return self.__plan_dao.getMaestros()