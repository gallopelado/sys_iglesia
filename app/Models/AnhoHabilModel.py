import json
class AnhoHabilModel:

    def __init__(self, anho_id=None, anho_des=None, estado=None):
        self.__anho_id = anho_id
        self.__anho_des = anho_des
        self.__estado = estado

    @property
    def anho_id(self):
        return self.__anho_id

    @anho_id.setter
    def anho_id(self, anho_id):
        self.__anho_id = anho_id

    @property
    def anho_des(self):
        return self.__anho_des

    @anho_des.setter
    def anho_des(self, anho_des):
        self.__anho_des = anho_des

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, estado):
        self.__estado = estado

    def __str__(self):
        return f'Anho_id: {self.anho_id}, Anho_des: {self.anho_des}, estado: {self.estado}'

    def __iter__(self):
        return self.__dict__
