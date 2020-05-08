class Asignatura:

    def __init__(self, id=None, nombre=None):
        self.__id = id
        self.__nombre = nombre

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    def __str__(self):
        return f"Id = {self.id}, Nombre= {self.nombre}"