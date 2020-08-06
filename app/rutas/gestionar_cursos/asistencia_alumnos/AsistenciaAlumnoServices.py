from datetime import datetime
from app.Models.gestionar_cursos.asistencia_alumno.AsistenciaAlumno_dao import AsistenciaAlumno_dao
from app.Models.gestionar_cursos.asistencia_alumno.AsistenciaCursoCab_model import AsistenciaCursoCab_model
from app.Models.gestionar_cursos.asistencia_alumno.AsistenciaCursoDet_model import AsistenciaCursoDet_model
class AsistenciaAlumnoServices:
    def __init__(self):
        self.__inscr = AsistenciaAlumno_dao()

    def getListaProfesorCursosAsignatura(self, idmalla, turno, idprofesor, idcurso, idasignatura, idnumeroasignatura):
        return self.__inscr.getListaProfesorCursosAsignatura(idmalla, turno, idprofesor, idcurso, idasignatura, idnumeroasignatura)

    def getCursosMaestro(self, idmalla, idprofesor):
        return self.__inscr.getCursosMaestro(idmalla, idprofesor)

    def getAsignaturaMaestro(self, idmalla, idprofesor, idcurso):
        return self.__inscr.getAsignaturaMaestro(idmalla, idprofesor, idcurso)

    def getListaAlumnosAsignatura(self, idmalla, cur_id, asi_id, num_id, turno):
        return self.__inscr.getListaAlumnosAsignatura(idmalla, cur_id, asi_id, num_id, turno)

    def registrarAsistencias(self, req):
        cabecera = AsistenciaCursoCab_model()
        cabecera.malla_id = req.json['malla_id']
        cabecera.cur_id = req.json['cur_id']
        cabecera.asi_id = req.json['asi_id']
        cabecera.num_id = req.json['num_id']
        cabecera.per_id = req.json['per_id']
        cabecera.turno = req.json['turno']
        cabecera.asiscurso_descripcion = req.json['descripcion']
        cabecera.asiscurso_estado = True
        cabecera.creacion_fecha = datetime.now()
        lista_detalle = {
            'asistieron':req.json['asistieron'] if 'asistieron' in req.json else None
            , 'puntuales': req.json['puntuales'] if 'puntuales' in req.json else None
        }
        self.__inscr.registrar(cabecera, lista_detalle)
        