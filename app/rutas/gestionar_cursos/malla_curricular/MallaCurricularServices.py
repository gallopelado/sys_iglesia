from datetime import date
from app.Models.gestionar_cursos.malla_curricular.MallaCurricular_dao import MallaCurricular_dao

class MallaCurricularServices:

    def obtenerTodasMallasCurriculares(self):
        malla_dao = MallaCurricular_dao()
        lista = malla_dao.obtenerMallaCurricular()
        lista_nueva = []
        for item in lista:
            nuevo = {}
            nuevo['idmalla'] = item['idmalla']
            nuevo['fecharegistro'] = item['fecharegistro']
            nuevo['estado'] = item['estado']
            nuevo['anho_id'] = item['anho_id']
            nuevo['anho_des'] = item['anho_des']
            if int(item['anho_des']) == int(date.today().year):                
                nuevo['botones'] = '''<button type="button" class="btn btn-primary btn-sm ver"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Ver</button> 
                <button type="button" class="btn btn-success btn-sm editar"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Modificar</button>'''
            else:
                nuevo['botones'] = '<button type="button" class="btn btn-primary btn-sm ver"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Ver</button>'
            lista_nueva.append(nuevo)
        return lista_nueva

    def obtenerTodasAreas(self):
        malla_dao = MallaCurricular_dao()
        return malla_dao.obtenerAreas()

    def obtenerTodasCursos(self):
        malla_dao = MallaCurricular_dao()
        return malla_dao.obtenerCursos()

    def obtenerAreaCursosAreaId(self, are_id):
        malla_dao = MallaCurricular_dao()
        return malla_dao.obtenerAreaCursos(are_id)

    def obtenerAnhoHabil(self):
        malla_dao = MallaCurricular_dao()
        return malla_dao.obtenerAnhoHabil()

    def obtenerCursosRegistrados(self, malla_id):
        malla_dao = MallaCurricular_dao()
        return malla_dao.obtenerCursosRegistrados(malla_id)

    def verificarAnhoHabil(self):
        malla_dao = MallaCurricular_dao()
        data = malla_dao.verificaMallaAnho()
        anio = date.today().year #anho actual
        if data:
            if int(data['anho_des']) == anio:
                return True
            else:
                return False

    def guardar(self, anho_id, cur_id, estado):
        malla_dao = MallaCurricular_dao()
        return malla_dao.guardarMallaCabecera(anho_id, cur_id, estado)

    def agregarNuevosCursosMalla(self, malla_id, cur_id, estado):
        malla_dao = MallaCurricular_dao()
        return malla_dao.agregarNuevosCursosMalla(malla_id, cur_id, estado)

    def anularCursoMalla(self, malla_id, cur_id, estado):
        malla_dao = MallaCurricular_dao()
        return malla_dao.anularCursoMalla(malla_id, cur_id, estado)

    def obtenerAsignaturasCurso(self, malla_id, cur_id):
        malla_dao = MallaCurricular_dao()
        return malla_dao.obtenerAsignaturasCurso(malla_id, cur_id)

    def obtenerTodasAsignaturas(self):
        malla_dao = MallaCurricular_dao()
        return malla_dao.obtenerTodasAsignaturas()

    def agregarNuevaAsignaturaCurso(self, malla_id, cur_id, asi_id, num_id, cant_horas):
        malla_dao = MallaCurricular_dao()
        return malla_dao.agregarNuevaAsignaturaCurso(malla_id, cur_id, asi_id, num_id, cant_horas)