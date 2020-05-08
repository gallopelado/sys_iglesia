class AreaModel:

    def __init__(self, area_id=None, area_des=None):
        self.__area_id = area_id
        self.__area_des = area_des
        self.__lista_cursos = []

    @property
    def area_id(self):
        return self.__area_id

    @area_id.setter
    def area_id(self, area_id):
        self.__area_id = area_id

    @property
    def area_des(self):
        return self.__area_des

    @area_des.setter
    def area_des(self, area_des):
        self.__area_des = area_des

    @property
    def lista_cursos(self):
        return self.__lista_cursos

    @lista_cursos.setter
    def lista_cursos(self, curso):
        self.__lista_cursos.append(curso)