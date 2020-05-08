class CursoModel:

    def __init__(self, curso_id=None, curso_des=None):
        self.__curso_id = curso_id
        self.__curso_des = curso_des

    @property
    def curso_id(self):
        return self.__curso_id

    @curso_id.setter
    def curso_id(self, curso_id):
        self.__curso_id = curso_id

    @property
    def curso_des(self):
        return self.__curso_des
    
    @curso_des.setter
    def curso_des(self, curso_des):
        self.__curso_des = curso_des

    def __str__(self):
        return f"Id = {self.curso_id}, Nombre= {self.curso_des}"
