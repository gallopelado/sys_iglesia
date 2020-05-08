class MallaCurricular:

    def __init__(self, malla_id=None, anhohabilmodel=None, fecharegistro=None, fechamodificacion=None
        , creacion_usuario=None,modificacion_usuario=None, estado=None):
        self.__malla_id = malla_id
        self.__anhohabilmodel = anhohabilmodel
        self.__fecharegistro = fecharegistro
        self.__fechamodificacion = fechamodificacion
        self.__creacion_usuario = creacion_usuario
        self.__modificacion_usuario = modificacion_usuario
        self.__estado = estado

    @property
    def malla_id(self):
        return self.__malla_id

    @malla_id.setter
    def malla_id(self, malla_id):
        self.__malla_id = malla_id

    @property
    def anhohabilmodel(self):
        return self.__anhohabilmodel

    @anhohabilmodel.setter
    def anhohabilmodel(self, anhohabilmodel):
        self.__anhohabilmodel = anhohabilmodel

    @property
    def fecharegistro(self):
        return self.__fecharegistro

    @fecharegistro.setter
    def fecharegistro(self, fecharegistro):
        self.__fecharegistro = fecharegistro

    @property
    def fechamodificacion(self):
        return self.__fechamodificacion

    @fechamodificacion.setter
    def fechamodificacion(self, fechamodificacion):
        self.__fechamodificacion = fechamodificacion

    @property
    def creacion_usuario(self):
        return self.__creacion_usuario

    @creacion_usuario.setter
    def creacion_usuario(self, creacion_usuario):
        self.__creacion_usuario = creacion_usuario

    @property
    def modificacion_usuario(self):
        return self.__modificacion_usuario
    
    @modificacion_usuario.setter
    def modificacion_usuario(self, modificacion_usuario):
        self.__modificacion_usuario = modificacion_usuario
    
    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, estado):
        self.__estado = estado

    def __str__(self):
        return f'''malla_id = {self.malla_id}, anhohabilmodel = {self.anhohabilmodel}
        , fecharegistro = {self.fecharegistro}, fechamodificacion = {self.fechamodificacion}
        , creacion_usuario = {self.creacion_usuario}, modificacion_usuario = {self.modificacion_usuario}
        , estado = {self.estado}'''
    