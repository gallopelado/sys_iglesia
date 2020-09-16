from app.Models.gestionar_cursos.desercion_alumnos.DesercionAlumno_dao import DesercionAlumno_dao

class DesercionServices:

    def __init__(self):
        self.__dese = DesercionAlumno_dao()

    def getCursosInscriptos(self):
        return self.__dese.getCursosInscriptos()

    def getListaAlumnos(self, cur_id):
        return self.__dese.getListaAlumnos(cur_id)
    
    def getMotivoDesercion(self):
        return self.__dese.getMotivoDesercion()

    def registrarDesercion(self, obj):
        return self.__dese.registrarDesercion(obj)