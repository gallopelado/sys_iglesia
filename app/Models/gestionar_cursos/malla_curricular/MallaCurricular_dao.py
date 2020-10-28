from app.Conexion.Conexion import Conexion
from app.Models.AreaModel import AreaModel
from app.Models.CursoModel import CursoModel
from app.Models.AnhoHabilModel import AnhoHabilModel
from app.Models.gestionar_cursos.malla_curricular.MallaCurricular import MallaCurricular

class MallaCurricular_dao(Conexion):

    def __init__(self):
        Conexion.__init__(self)
    
    def guardarMallaCabecera(self, anho_id, cur_id, estado):

        bandera = False
        insertSQL_cab = '''INSERT INTO cursos.malla_curricular
        (anho_id, creacion_fecha, creacion_usuario, modificacion_fecha, modificacion_usuario, estado)
        VALUES(%s, now(), NULL, NULL, NULL, true) RETURNING malla_id
        '''
        insertSQL_det = '''INSERT INTO cursos.detalle_malla_curricular
                (malla_id, cur_id, estado)
                VALUES(%s, %s, %s);'''

        try:
            con = self.getConexion()
            con.autocommit = False
            cur = con.cursor()
            cur.execute(insertSQL_cab, (anho_id,))
            malla_id = cur.fetchone()[0]
            cur.execute(insertSQL_det, (malla_id, cur_id, estado,))
            con.commit()
            bandera = True
        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()
        return bandera

    def agregarNuevosCursosMalla(self, malla_id, cur_id, estado):
        bandera = False
        insertSQL_det = '''INSERT INTO cursos.detalle_malla_curricular
                        (malla_id, cur_id, estado)
                        VALUES(%s, %s, %s);'''
        try:
            con = self.getConexion()
            cur = con.cursor()
            cur.execute(insertSQL_det, (malla_id, cur_id, estado,))
            con.commit()
            bandera = True
        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()
        return bandera

    def anularCursoMalla(self, malla_id, cur_id, estado):
        bandera = False
        updateSQL = '''UPDATE cursos.detalle_malla_curricular
                        SET estado = %s WHERE malla_id = %s AND cur_id = %s'''
        try:
            con = self.getConexion()
            cur = con.cursor()
            cur.execute(updateSQL, (estado, malla_id, cur_id))
            con.commit()
            bandera = True
        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()
        return bandera

    def agregarNuevaAsignaturaCurso(self, malla_id, cur_id, asi_id, num_id, cant_horas):
        bandera = False
        insertSQL_det = '''INSERT INTO cursos.curso_asignaturas
        (malla_id, cur_id, asi_id, num_id, estado, cant_horas)
        VALUES(%s, %s, %s, %s, true, %s) ON CONFLICT (malla_id, cur_id, asi_id, num_id) DO
        UPDATE SET cant_horas = EXCLUDED.cant_horas
        '''
        try:
            con = self.getConexion()
            cur = con.cursor()
            cur.execute(insertSQL_det, (malla_id, cur_id, asi_id, num_id, cant_horas))
            con.commit()
            bandera = True
        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()
        return bandera

    def anularAsignaturaCurso(self, malla_id, cur_id, asi_id, num_id):
        bandera = False
        insertSQL_det = '''UPDATE cursos.curso_asignaturas SET
        estado = FALSE WHERE malla_id = %s AND cur_id = %s AND asi_id = %s AND num_id = %s'''
        try:
            con = self.getConexion()
            cur = con.cursor()
            cur.execute(insertSQL_det, (malla_id, cur_id, asi_id, num_id,))
            con.commit()
            bandera = True
        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()
        return bandera

    def obtenerAreas(self):
        lista_areas = []
        querySQL = 'SELECT are_id, are_des from referenciales.areas'

        try:
            con = self.getConexion()
            cur = con.cursor()
            cur.execute(querySQL)
            data = cur.fetchall()

            for rs in data:
                area = {}
                area['area_id'] = rs[0]
                area['area_des'] = rs[1]
                lista_areas.append(area)

        except con.Error as e:
            print(e)
        finally:
            if con is not None:
                cur.close()
                con.close()
        return lista_areas

    def obtenerCursos(self):
        lista_cursos = []
        querySQL = 'SELECT cur_id, cur_des FROM referenciales.cursos'

        try:
            con = self.getConexion()
            cur = con.cursor()
            cur.execute(querySQL)
            data = cur.fetchall()
            for rs in data:
                curso = {}
                curso['cur_id'] = rs[0]
                curso['cur_des'] = rs[1]
                lista_cursos.append(curso)

        except con.Error as e:
            print(e)
        finally:
            if con is not None:
                cur.close()
                con.close()
        return lista_cursos

    def obtenerAreaCursos(self, area_id):
        lista_cursos = []
        querySQL = '''SELECT are_id, are_des, cur_id, cur_des FROM referenciales.area_cursos ac 
            LEFT JOIN referenciales.areas a USING(are_id) LEFT JOIN referenciales.cursos cu USING(cur_id)
            WHERE are_id = %s
            '''

        try:
            con = self.getConexion()
            cur = con.cursor()
            cur.execute(querySQL, (area_id,))
            data = cur.fetchall()
            print(data)
            for rs in data:
                area_curso = {}
                area_curso['are_id'] = rs[0]
                area_curso['are_des'] = rs[1]
                area_curso['cur_id'] = rs[2]
                area_curso['cur_des'] = rs[3]
                lista_cursos.append(area_curso)

        except con.Error as e:
            print(e)
        finally:
            if con is not None:
                cur.close()
                con.close()
        return lista_cursos

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

    def obtenerCursosRegistrados(self, malla_id):
        lista =[]
        querySQL = '''SELECT malla_id, cur_id, cur_des, are_id, are_des 
        FROM cursos.detalle_malla_curricular ma
        LEFT JOIN referenciales.cursos USING(cur_id)
        LEFT join referenciales.area_cursos USING(cur_id)
        LEFT join referenciales.areas using(are_id) WHERE malla_id = %s and ma.estado IS TRUE'''
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(querySQL, (malla_id,))
            data = cur.fetchall()
            for rs in data:
                objeto = {}
                objeto['malla_id'] = rs[0]
                objeto['cur_id'] = rs[1]
                objeto['cur_des'] = rs[2]
                objeto['are_id'] = rs[3]
                objeto['are_des'] = rs[4]
                lista.append(objeto)

        except con.Error as e:
            print(e)
        finally:
            if con is not None:
                cur.close()
                con.close()

        return lista

    def verificaMallaAnho(self):
        objeto = {}
        querySQL = '''select mc.anho_id, an.anho_des, mc.malla_id, mc.estado from cursos.malla_curricular mc
        left join referenciales.anho_habil an on mc.anho_id = an.anho_id 
        where mc.estado is true and an.is_active is true'''

        try:
            con = self.getConexion()
            cur = con.cursor()
            cur.execute(querySQL)
            data = cur.fetchall()
            if data:
                for rs in data:
                    objeto['anho_id'] = rs[0]
                    objeto['anho_des'] = rs[1]
                    objeto['malla_id'] = rs[2]
                    objeto['estado'] = rs[3]


        except con.Error as e:
            print(e)
        finally:
            if con is not None:
                cur.close()
                con.close()

        return objeto

    def obtenerAnhoHabil(self):
        data_anho = {}
        querySQL = '''SELECT anho_id, anho_des, is_active FROM referenciales.anho_habil
                    WHERE is_active IS TRUE'''

        try:
            con = self.getConexion()
            cur = con.cursor()
            cur.execute(querySQL)
            data = cur.fetchone()
            data_anho['anho_id'] = data[0]
            data_anho['anho_des'] = data[1]
            data_anho['is_active'] = data[2]

        except con.Error as e:
            print(e)
        finally:
            if con is not None:
                cur.close()
                con.close()

        return data_anho

    def obtenerAsignaturasCurso(self, malla_id, cur_id):
        lista = []
        querySQL = '''SELECT 
            ca.malla_id
            , cu.cur_id, cu.cur_des 
            , asi.asi_id, asi.asi_des 
            , num.num_id, num.num_des, ca.cant_horas 
        FROM cursos.curso_asignaturas ca 
        LEFT JOIN referenciales.cursos cu ON cu.cur_id = ca.cur_id 
        LEFT JOIN referenciales.asignaturas  asi ON asi.asi_id = ca.asi_id
        LEFT JOIN referenciales.numero_asignatura num ON num.num_id = ca.num_id 
        WHERE ca.malla_id = %s AND cu.cur_id = %s AND ca.estado IS TRUE'''

        try:
            con = self.getConexion()
            cur = con.cursor()
            cur.execute(querySQL, (malla_id, cur_id,))
            data = cur.fetchall()
            for rs in data:
                objeto = {}
                objeto['malla_id'] = rs[0]
                objeto['cur_id'] = rs[1]
                objeto['cur_des'] = rs[2]
                objeto['asi_id'] = rs[3]
                objeto['asi_des'] = rs[4]
                objeto['num_id'] = rs[5]
                objeto['num_des'] = rs[6]
                objeto['cant_horas'] = rs[7]
                lista.append(objeto)
        except con.Error as e:
            print(e)
        finally:
            if con is not None:
                cur.close()
                con.close()

        return lista

    def obtenerTodasAsignaturas(self):
        lista = []
        querySQL = '''SELECT 
            ast.asi_id , asi.asi_des , ast.num_id, num.num_des 
        FROM referenciales.asignatura_tomo ast 
        LEFT JOIN referenciales.asignaturas asi on asi.asi_id = ast.asi_id 
        LEFT JOIN referenciales.numero_asignatura num on num.num_id = ast.num_id '''

        try:
            con = self.getConexion()
            cur = con.cursor()
            cur.execute(querySQL)
            data = cur.fetchall()
            for rs in data:
                objeto = {}
                objeto['asi_id'] = rs[0]
                objeto['asi_des'] = rs[1]
                objeto['num_id'] = rs[2]
                objeto['num_des'] = rs[3]
                lista.append(objeto)
        except con.Error as e:
            print(e)
        finally:
            if con is not None:
                cur.close()
                con.close()

        return lista