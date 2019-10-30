from app.Conexion.Conexion import Conexion

class ObreroModel:
    def traerPostulacionesProcesadasPorMinisterio(self, idcomite):
        consulta = '''
        SELECT 
            DISTINCT(cp.post_id)
            , cp.post_des descripcion, to_char(post_fechacalificado, 'DD "de" TMMonth "del" YYYY') fechacalificado 
            , min_id idministerio
            , min_des ministerio
            , COUNT(ca.mo_id) cantidad_admitidos
        FROM 
            membresia.cabe_postulacion AS cp 
        LEFT JOIN 
            membresia.candi_admitidos AS ca ON cp.post_id = ca.post_id
        LEFT JOIN 
            referenciales.ministerios AS min using(min_id)
        WHERE 
            post_fechacalificado IS NOT NULL
        GROUP BY cp.post_id, min_des, cp.post_fechacalificado
        HAVING min_id = %s

        '''
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.execute(consulta, (idcomite,))
            return cur.fetchall()
        except con.Error as e:
            print(e.pgerror)
            return False
        finally:
            if con is not None:
                cur.close()
                con.close()


    def traerCalificadosPorPostulacion(self, idpostulacion):
        funcion = 'membresia.traer_calificados_por_postulacion'
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.callproc(funcion, (idpostulacion,))
            return cur.fetchone()[0]
        except con.Error as e:
            print(e.pgerror)
            return False
        finally:
            if con is not None:
                cur.close()
                con.close()