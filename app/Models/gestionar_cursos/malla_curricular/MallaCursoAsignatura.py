from app.Models.gestionar_cursos.DetalleMallaCurricular import DetalleMallaCurricular
from app.Models.AsignaturaModel import Asignatura

class MallaCursoAsignatura:

    def __init__(self, malla_id=None, anhohabilmodel=None, fecharegistro=None, fechamodificacion=None
        , creacion_usuario=None,modificacion_usuario=None, estado=None, curso_id=None, curso_des=None
        , estado_detalle=None, id=None, nombre=None, estado_malla_curso_asignatura = None):

        self.__detalle_malla = DetalleMallaCurricular(malla_id, anhohabilmodel, fecharegistro, fechamodificacion
        , creacion_usuario,modificacion_usuario, estado, curso_id, curso_des, estado_detalle)
        self.__asignatura = Asignatura(id, nombre)
        self.__estado_malla_curso_asignatura = estado_malla_curso_asignatura

    @property
    def malla_id(self):
        return self.__detalle_malla.malla_id

    @malla_id.setter
    def malla_id(self, malla_id):
        self.__detalle_malla.malla_id = malla_id

    @property
    def anhohabilmodel(self):
        return self.__detalle_malla.anhohabilmodel

    @anhohabilmodel.setter
    def anhohabilmodel(self, anhohabilmodel):
        self.__detalle_malla.anhohabilmodel = anhohabilmodel

    @property
    def fecharegistro(self):
        return self.__detalle_malla.fecharegistro

    @fecharegistro.setter
    def fecharegistro(self, fecharegistro):
        self.__detalle_malla.fecharegistro = fecharegistro

    @property
    def fechamodificacion(self):
        return self.__detalle_malla.fechamodificacion

    @fechamodificacion.setter
    def fechamodificacion(self, fechamodificacion):
        self.__detalle_malla.fechamodificacion = fechamodificacion
    
    @property
    def creacion_usuario(self):
        return self.__detalle_malla.creacion_usuario

    @creacion_usuario.setter
    def creacion_usuario(self, creacion_usuario):
        self.__detalle_malla.creacion_usuario = creacion_usuario
    
    @property
    def modificacion_usuario(self):
        return self.__detalle_malla.modificacion_usuario

    @modificacion_usuario.setter
    def modificacion_usuario(self, modificacion_usuario):
        self.__detalle_malla.modificacion_usuario = modificacion_usuario

    @property
    def estado(self):
        return self.__detalle_malla.estado

    @estado.setter
    def estado(self, estado):
        self.__detalle_malla.estado = estado

    @property
    def curso_id(self):
        return self.__detalle_malla.curso_id

    @curso_id.setter
    def curso_id(self, curso_id):
        self.__detalle_malla.curso_id = curso_id

    @property
    def curso_des(self):
        return self.__detalle_malla.curso_des

    @curso_des.setter
    def curso_des(self, curso_des):
        self.__detalle_malla.curso_des = curso_des

    @property
    def estado_detalle(self):
        return self.__detalle_malla.estado_detalle

    @estado_detalle.setter
    def estado_detalle(self, estado_detalle):
        self.__detalle_malla.estado_detalle = estado_detalle

    @property
    def id_asignatura(self):
        return self.__asignatura.id

    @id_asignatura.setter
    def id_asignatura(self, id):
        self.__asignatura.id = id

    @property
    def nombre_asignatura(self):
        return self.__asignatura.nombre

    @nombre_asignatura.setter
    def nombre_asignatura(self, nombre_asignatura):
        self.__asignatura.nombre = nombre_asignatura

    @property
    def estado_malla_curso_asignatura(self):
        return self.__estado_malla_curso_asignatura

    @estado_malla_curso_asignatura.setter
    def estado_malla_curso_asignatura(self, estado_malla_curso_asignatura):
        self.__estado_malla_curso_asignatura = estado_malla_curso_asignatura

    def __str__(self):
        return f'''malla_id={self.malla_id}, anhohabilmodel={self.anhohabilmodel}, fecharegistro={self.fecharegistro}, fechamodificacion={self.fechamodificacion}
        , creacion_usuario={self.creacion_usuario}, modificacion_usuario={self.modificacion_usuario}, estado={self.estado}, curso_id={self.curso_id}, curso_des={self.curso_des}
        , estado_detalle={self.estado_detalle}, id_asignatura={self.id_asignatura}, nombre_asignatura={self.nombre_asignatura}, estado_malla_curso_asignatura = {self.estado_malla_curso_asignatura}'''