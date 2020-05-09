from datetime import date
from app.Models.gestionar_cursos.malla_curricular.MallaCurricular_dao import MallaCurricular_dao

class MallaCurricularServices:

    def obtenerTodasMallasCurriculares(self):
        malla_dao = MallaCurricular_dao()
        return malla_dao.obtenerMallaCurricular()

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