from app.Models.gestionar_cursos.malla_curricular.MallaCurricular import MallaCurricular
from app.Models.CursoModel import CursoModel

class DetalleMallaCurricular:

    def __init__(self, malla_id=None, anhohabilmodel=None, fecharegistro=None, fechamodificacion=None
        , creacion_usuario=None,modificacion_usuario=None, estado=None, curso_id=None, curso_des=None, estado_detalle=None):
       self.__mallacurricular = MallaCurricular(malla_id, anhohabilmodel, fecharegistro, fechamodificacion
       , creacion_usuario, modificacion_usuario, estado)
       self.__curso =  CursoModel(curso_id, curso_des)
       self.__estado_detalle = estado_detalle

    @property
    def malla_id(self):
        return self.__mallacurricular.malla_id

    @malla_id.setter
    def mallacurricular(self, malla_id):
        self.__mallacurricular.malla_id = malla_id

    @property
    def anhohabilmodel(self):
        return self.__mallacurricular.anhohabilmodel

    @anhohabilmodel.setter
    def anhohabilmodel(self, anhohabilmodel):
        self.__mallacurricular.anhohabilmodel = anhohabilmodel

    @property
    def fecharegistro(self):
        return self.__mallacurricular.fecharegistro

    @fecharegistro.setter
    def fecharegistro(self, fecharegistro):
        self.__mallacurricular.fecharegistro = fecharegistro

    @property
    def fechamodificacion(self):
        return self.__mallacurricular.fechamodificacion

    @fechamodificacion.setter
    def fechamodificacion(self, fechamodificacion):
        self.__mallacurricular.fechamodificacion = fechamodificacion

    @property
    def creacion_usuario(self):
        return self.__mallacurricular.creacion_usuario

    @creacion_usuario.setter
    def creacion_usuario(self, creacion_usuario):
        self.__mallacurricular.creacion_usuario = creacion_usuario

    @property
    def modificacion_usuario(self):
        return self.__mallacurricular.modificacion_usuario
    
    @modificacion_usuario.setter
    def modificacion_usuario(self, modificacion_usuario):
        self.__mallacurricular.modificacion_usuario = modificacion_usuario

    @property
    def estado(self):
        return self.__mallacurricular.estado

    @estado.setter
    def estado(self, estado):
        self.__mallacurricular.estado = estado

    ## Getters y setters de CursoModel
    @property
    def curso_id(self):
        return self.__curso.curso_id

    @curso_id.setter
    def curso_id(self, curso_id):
        self.__curso.curso_id = curso_id

    @property
    def curso_des(self):
        return self.__curso.curso_des

    @curso_des.setter
    def curso_des(self, curso_des):
        self.__curso_des = curso_des

    # Estado del detalle
    @property
    def estado_detalle(self):
        return self.__estado_detalle

    @estado_detalle.setter
    def estado_detalle(self, estado_detalle):
        self.__estado_detalle = estado_detalle

    def __str__(self):
        return f'''malla_id={self.malla_id},  anhohabilmodel={self.anhohabilmodel.__str__}
        , fecharegistro={self.fecharegistro}, fechamodificacion={self.fechamodificacion}
        , creacion_usuario={self.creacion_usuario}, modificacion_usuario={self.modificacion_usuario}
        , estado={self.estado}, curso_id={self.curso_id}, curso_des={self.curso_des}
        , estado_detalle={self.estado_detalle}'''