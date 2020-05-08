from app.Models.gestionar_cursos.malla_curricular.MallaCurricular_dao import MallaCurricular_dao

class MallaCurricularServices:

    def obtenerTodasMallasCurriculares(self):

        malla_dao = MallaCurricular_dao()
        return malla_dao.obtenerMallaCurricular()