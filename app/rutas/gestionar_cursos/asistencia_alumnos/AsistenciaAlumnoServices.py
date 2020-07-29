from app.Models.gestionar_cursos.asistencia_alumno.AsistenciaAlumno_dao import AsistenciaAlumno_dao
class AsistenciaAlumnoServices:
    def __init__(self):
        self.__inscr = AsistenciaAlumno_dao()

    def getListaProfesorCursosAsignatura(self, idmalla, turno, idprofesor):
        return self.__inscr.getListaProfesorCursosAsignatura(idmalla, turno, idprofesor)

    def getListaAlumnosAsignatura(self, idmalla, cur_id, asi_id, num_id, turno):
        return self.__inscr.getListaAlumnosAsignatura(idmalla, cur_id, asi_id, num_id, turno)