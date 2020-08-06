class AsistenciaCursoCab_model:
    def __init__(self, asiscurso_id=None, malla_id=None, asi_id=None, num_id=None, per_id=None, turno=None, cur_id=None, asiscurso_descripcion=None
        , creacion_fecha=None, creacion_usuario=None, modificacion_fecha=None, modificacion_usuario=None, asiscurso_estado=None):
        self.__asiscurso_id = asiscurso_id
        self.__malla_id = malla_id
        self.__asi_id = asi_id
        self.__num_id = num_id
        self.__per_id = per_id
        self.__turno = turno
        self.__cur_id = cur_id
        self.__asiscurso_descripcion = asiscurso_descripcion
        self.__creacion_fecha = creacion_fecha
        self.__creacion_usuario = creacion_usuario
        self.__modificacion_fecha = modificacion_fecha
        self.__modificacion_usuario = modificacion_usuario
        self.__asiscurso_estado = asiscurso_estado

    @property
    def asiscurso_id(self):
        return self.__asiscurso_id
    @asiscurso_id.setter
    def asiscurso_id(self, asiscurso_id):
        self.__asiscurso_id = asiscurso_id

    @property
    def malla_id(self):
        return self.__malla_id
    @malla_id.setter
    def malla_id(self, malla_id):
        self.__malla_id = malla_id

    @property
    def asi_id(self):
        return self.__asi_id
    @asi_id.setter
    def asi_id(self, asi_id):
        self.__asi_id = asi_id

    @property
    def num_id(self):
        return self.__num_id
    @num_id.setter
    def num_id(self, num_id):
        self.__num_id = num_id
    
    @property
    def per_id(self):
        return self.__per_id
    @per_id.setter
    def per_id(self, per_id):
        self.__per_id = per_id

    @property
    def turno(self):
        return self.__turno
    @turno.setter
    def turno(self, turno):
        self.__turno = turno

    @property
    def cur_id(self):
        return self.__cur_id
    @cur_id.setter
    def cur_id(self, cur_id):
        self.__cur_id = cur_id

    @property
    def asiscurso_descripcion(self):
        return self.__asiscurso_descripcion
    @asiscurso_descripcion.setter
    def asiscurso_descripcion(self, asiscurso_descripcion):
        self.__asiscurso_descripcion = asiscurso_descripcion

    @property
    def creacion_fecha(self):
        return self.__creacion_fecha
    @creacion_fecha.setter
    def creacion_fecha(self, creacion_fecha):
        self.__creacion_fecha = creacion_fecha

    @property
    def creacion_usuario(self):
        return self.__creacion_usuario
    @creacion_usuario.setter
    def creacion_usuario(self, creacion_usuario):
        self.__creacion_usuario = creacion_usuario

    @property
    def modificacion_fecha(self):
        return self.__modificacion_fecha
    @modificacion_fecha.setter
    def modificacion_fecha(self, modificacion_fecha):
        self.__modificacion_fecha = modificacion_fecha

    @property
    def modificacion_usuario(self):
        return self.__modificacion_usuario
    @modificacion_usuario.setter
    def modificacion_usuario(self, modificacion_usuario):
        self.__modificacion_usuario = modificacion_usuario

    @property
    def asiscurso_estado(self):
        return self.__asiscurso_estado
    @asiscurso_estado.setter
    def asiscurso_estado(self, asiscurso_estado):
        self.__asiscurso_estado = asiscurso_estado

    def __str__(self):
        return f'''asiscurso_id={self.asiscurso_id}, malla_id={self.malla_id}, asi_id={self.asi_id}
        , num_id={self.num_id}, per_id={self.per_id}, turno={self.turno}, cur_id={self.cur_id}, asiscurso_descripcion={self.asiscurso_descripcion}
        , creacion_fecha={self.creacion_fecha}, creacion_usuario={self.creacion_usuario}, modificacion_fecha={self.modificacion_fecha}
        , modificacion_usuario={self.modificacion_usuario}, asiscurso_estado={self.asiscurso_estado}'''
