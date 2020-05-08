from app.Conexion.Conexion import Conexion
from app.Models.AreaModel import AreaModel
from app.Models.CursoModel import CursoModel
from app.Models.AnhoHabilModel import AnhoHabilModel
from app.Models.gestionar_cursos.malla_curricular.MallaCurricular import MallaCurricular

class MallaCurricular_dao(Conexion):

    def __init__(self):
        Conexion.__init__(self)
    
    def guardarMallaCabecera(self, mc=None):

        insertSQL=''

        try:
            con = self.getConexion()
            cur = con.cursor()
            cur.execute(insertSQL)
            con.commit()

        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()

    def guardarMallaDetalle(self, dmc=None):

       insertSQL = ''

       try:
        
           con = self.getConexion()
           cur = con.cursor()
           cur.execute(insertSQL)
           con.commit()

       except con.Error as e:
           print(e)
       finally:
           if con is not None:
               cur.close()
               con.close()

    def obtenerArea(self):
        lista_areas = []
        querySQL = ''

        try:
            con = self.getConexion()
            cur = con.cursor()
            cur.execute(querySQL)
            data = cur.fetchall()
            for rs in data:
                area = AreaModel(rs[0], rs[1])
                lista_areas.append(area)

        except con.Error as e:
            print(e)
        finally:
            if con is not None:
                cur.close()
                con.close()

    def obtenerCurso(self):
        lista_cursos = []
        querySQL = ''

        try:
            con = self.getConexion()
            cur = con.cursor()
            cur.execute(querySQL)
            data = cur.fetchall()
            for rs in data:
                curso = CursoModel(rs[0], rs[1])
                lista_cursos.append(curso)

        except con.Error as e:
            print(e)
        finally:
            if con is not None:
                cur.close()
                con.close()

    def obtenerMallaCurricular(self):
        mallas =[]
        querySQL = '''SELECT 
                malla_id
                , to_char(creacion_fecha, 'DD/MM/YYYY')fecharegistro
                , estado 
                , anho_id, anho_des
            FROM cursos.malla_curricular mc 
            LEFT JOIN referenciales.anho_habil USING(anho_id)'''

        try:
            con = self.getConexion()
            cur = con.cursor()
            cur.execute(querySQL)
            data = cur.fetchall()
            for rs in data:
                #print(rs)
                lista = {}
                lista['idmalla'] = rs[0]
                lista['fecharegistro'] = rs[1]
                lista['estado'] = 'ACTIVO' if rs[2] else 'INACTIVO'
                lista['anho_id'] = rs[3]
                lista['anho_des'] = rs[4]
                mallas.append(lista)

        except con.Error as e:
            print(e)
        finally:
            if con is not None:
                cur.close()
                con.close()

        return mallas