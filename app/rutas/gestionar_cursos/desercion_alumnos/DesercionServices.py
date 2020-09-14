from app.Models.gestionar_cursos.desercion_alumnos.DesercionAlumno_dao import DesercionAlumno_dao

class DesercionServices:

    def __init__(self):
        self.__dese = DesercionAlumno_dao()

    def getMaestros(self):
        return self.__dese.getMaestros()

    def getCursoMaestro(self, perid, turno):
        return self.__dese.getCursoMaestro(perid, turno)

    def registrarDesercion(self, obj):
        return self.__dese.registrarDesercion(obj)