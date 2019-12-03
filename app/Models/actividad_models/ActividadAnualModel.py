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
