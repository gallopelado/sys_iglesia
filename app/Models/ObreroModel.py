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

    
    def procesarObrero(self, opcion, idcomite, idpersona, idpostulacion, entrena, obs, motivo_baja, motivo_reincorporacion, idusuario):
        procedimiento = 'CALL membresia.gestionar_obreros(%s, %s, %s, %s, %s, %s, %s, %s, %s)'
        parametros = (opcion, idcomite, idpersona, idpostulacion, entrena, obs, motivo_baja, motivo_reincorporacion, idusuario,)
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.execute(procedimiento, parametros)
            con.commit()
            return True
        except con.Error as e:
            print(e.pgerror)
            return False
        finally:
            if con is not None:
                cur.close()
                con.close()


    def traerObrerosPorComite(self, idcomite, estado):
        funcion = 'membresia.traer_obreros_por_comite'
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.callproc(funcion, (idcomite, estado))            
            return cur.fetchall()
        except con.Error as e:
            print(e.pgerror)
            return False
        finally:
            if con is not None:
                cur.close()
                con.close()


    def traerObrerosPorComiteId(self, idcomite, idobrero):
        funcion = 'membresia.traer_obreros_por_comite_id'
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.callproc(funcion, (idcomite,idobrero,))            
            return cur.fetchall()[0]
        except con.Error as e:
            print(e.pgerror)
            return False
        finally:
            if con is not None:
                cur.close()
                con.close()