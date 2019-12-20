from app.Conexion.Conexion import Conexion


class ActividadAnualModel:

    def obtenerAnho(self):
        try:
            consulta = 'select anho_id idanho, anho_des anho, is_active activo from referenciales.anho_habil'
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.execute(consulta)
            return cur.fetchall()
        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()

    def obtenerActividadesJson(self, anho):
        try:
            consulta = '''
            SELECT array_to_json(array_agg(row_to_json(datos)))
            FROM (
                SELECT idactividad
                        , anho
                        , evento
                        , fecha_formatolargo(fechainicio)fechainicio
                        , fecha_formatolargo(fechafin)fechafin 
                FROM actividades.get_actividades(%s))datos;
            '''
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.execute(consulta, (anho,))            
            return cur.fetchone()[0]
        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()

    def verificarAnho(self, anho):
        try:
            consulta = 'actividades.verificar_anho'
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.callproc(consulta, (anho,))            
            return cur.fetchone()[0]
        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()

    def verificarAnhoFuturo(self, anho):
        try:
            consulta = 'SELECT anho_id FROM referenciales.anho_habil WHERE anho_des = %s AND is_active = FALSE AND adelantar = TRUE'
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.execute(consulta, (anho,))  
            resultado = cur.fetchone() is not None if True else False                     
            return resultado
        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()

    def verificarAnhoActivo(self, anho):
        try:
            consulta = 'SELECT anho_des FROM referenciales.anho_habil WHERE is_active = TRUE AND adelantar = FALSE'
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.execute(consulta, (anho,))  
            resultado = cur.fetchone()[0]                                
            return resultado
        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()
