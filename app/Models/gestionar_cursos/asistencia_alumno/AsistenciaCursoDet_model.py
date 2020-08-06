class AsistenciaCursoDet_model:
    def __init__(self, asiscurso_id=None, per_id=None, asiscursodet_asistio=None, asiscursodet_puntual=None, asiscursodet_estado=None):
        self.__asiscurso_id = asiscurso_id
        self.__per_id = per_id
        self.__asiscursodet_asistio = asiscursodet_asistio
        self.__asiscursodet_puntual = asiscursodet_puntual
        self.__asiscursodet_estado = asiscursodet_estado
    
    @property
    def asiscurso_id(self):
        return self.__asiscurso_id
    @asiscurso_id.setter
    def asiscurso_id(self, asiscurso_id):
        self.__asiscurso_id = asiscurso_id
    
    @property
    def per_id(self):
        return self.__per_id
    @per_id.setter
    def per_id(self, per_id):
        self.__per_id = per_id
    
    @property
    def asiscursodet_asistio(self):
        return self.__asiscursodet_asistio
    @asiscursodet_asistio.setter
    def asiscursodet_asistio(self, asiscursodet_asistio):
        self.__asiscursodet_asistio = asiscursodet_asistio

    @property
    def asiscursodet_puntual(self):
        return self.__asiscursodet_puntual
    @asiscursodet_puntual.setter
    def asiscursodet_puntual(self, asiscursodet_puntual):
        self.__asiscursodet_puntual = asiscursodet_puntual

    @property
    def asiscursodet_estado(self):
        return self.__asiscursodet_estado
    @asiscursodet_estado.setter
    def asiscursodet_estado(self, asiscursodet_estado):
        self.__asiscursodet_estado = asiscursodet_estado

    def __str__(self):
        return f'''asiscurso_id={self.asiscurso_id}, per_id={self.per_id}, asiscursodet_asistio={self.asiscursodet_asistio}
        , asiscursodet_puntual={self.asiscursodet_puntual}, asiscursodet_estado={self.asiscursodet_estado}'''