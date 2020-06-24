from app.Models.gestionar_cursos.inscripcion_alumnos.InscripcionAlumno_dao import InscripcionAlumno_dao

class InscripcionAlumnoServices:

    def __init__(self):
        self.__ins_dao = InscripcionAlumno_dao()

    def getCursosPlanificados(self):
        nuevo = []
        lista = self.__ins_dao.getCursosPlanificados()
        if len(lista) > 0:
            for item in lista:
                obj = {}
                obj['malla_id'] = item['malla_id']
                obj['estado'] = item['estado']
                obj['cur_id'] = item['cur_id']
                obj['curso'] = item['curso']
                obj['btn_inscribir'] = '<button type="button" class="btn btn-success btn-sm inscribir"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Inscribir</button>'
                nuevo.append(obj)
        return nuevo

    def getPersonas(self):
        return self.__ins_dao.getPersonas()

    def getListaAlumnosRegistrados(self, malla_id, curso_id):
        return self.__ins_dao.getListaAlumnosRegistradosInscripcion(malla_id, curso_id)

    def inscribirAlumnoCurso(self, alumno):
       return self.__ins_dao.insertarAlumno(alumno) 

    def actualizarEstadoInscripcionAlumno(self, alumno):
       return self.__ins_dao.actualizarEstadoInscripcionAlumno(alumno) 

    def obtenerAsignaturas(self, malla_id, curso_id):
        return self.__ins_dao.obtenerAsignaturas(malla_id, curso_id)

    def obtenerAsignaturasAlumno(self, malla_id, curso_id, per_id):
        return self.__ins_dao.obtenerAsignaturasAlumno(malla_id, curso_id, per_id)

    def guardarAsignaturaAlumno(self, res):
        return self.__ins_dao.guardarAsignaturaAlumno(res)

    def anularAsignaturaAlumno(self, res):
        return self.__ins_dao.anularAsignaturaAlumno(res)