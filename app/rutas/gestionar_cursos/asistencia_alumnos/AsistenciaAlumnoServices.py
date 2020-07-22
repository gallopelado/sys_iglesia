from app.Models.gestionar_cursos.asistencia_alumno.AsistenciaAlumno_dao import AsistenciaAlumno_dao
class AsistenciaAlumnoServices:
    def __init__(self):
        self.__inscr = AsistenciaAlumno_dao()

    def getListaProfesorCursosAsignatura(self, turno, idprofesor):
        return self.__inscr.getListaProfesorCursosAsignatura(turno, idprofesor)