from flask import current_app as app
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

    def getListaObrerosByComite(self, min_id, fechadesde, fechahasta, entrenamiento, estado):
        lista=[]
        querySQL = '''
            SELECT 
                co.min_id,
                co.per_id, CONCAT(p.per_nombres, ' ', p.per_apellidos)obrero, 
                co.fecha_ingreso, 
                CASE co.entrenamiento WHEN true THEN 'SI' ELSE 'NO' END entrenamiento, 
                CASE TRIM(co.observacion) WHEN NULL THEN 'SIN DESCRIPCION' WHEN '' THEN 'SIN DESCRIPCION' ELSE COALESCE(TRIM(co.observacion), 'SIN DESCRIPCION') END observacion, 
                CASE co.estado WHEN TRUE THEN 'SI' ELSE 'NO' END estado,
                co.motivo_baja, 
                co.motivo_reincorporacion, m.min_des
            FROM 
                membresia.comite_obreros co
            left join referenciales.personas p on p.per_id = co.per_id
            left join referenciales.ministerios m on m.min_id=co.min_id'''
        if min_id and entrenamiento and estado:
            querySQL += ''' where co.min_id=%s and co.estado=%s and co.entrenamiento=%s'''
        elif not min_id and entrenamiento and estado and fechadesde and fechahasta:
            querySQL += ''' where co.estado=%s and co.entrenamiento=%s AND co.fecha_ingreso BETWEEN %s AND %s'''
        elif min_id and entrenamiento and estado and fechadesde and fechahasta:
            querySQL += ''' where co.min_id=%s and co.estado=%s and co.entrenamiento=%s AND co.fecha_ingreso BETWEEN %s AND %s'''

        conexion = Conexion()
        conn = conexion.getConexion()
        cur = conn.cursor()
        try:
            if min_id and entrenamiento and estado:
                cur.execute(querySQL, (min_id, estado, entrenamiento,))
            elif not min_id and entrenamiento and estado and fechadesde and fechahasta:
                cur.execute(querySQL, (estado, entrenamiento, fechadesde, fechahasta,))
            elif min_id and entrenamiento and estado and fechadesde and fechahasta:
                cur.execute(querySQL, (min_id, estado, entrenamiento, fechadesde, fechahasta,))
            else:
                cur.execute(querySQL)
            data = cur.fetchall()
            if len(data) > 0:
                for rs in data:
                    obj = {}
                    obj['min_id'] = rs[0]
                    obj['per_id'] = rs[1]
                    obj['obrero'] = rs[2]
                    obj['fecha_ingreso'] = rs[3]
                    obj['entrenamiento'] = rs[4]
                    obj['observacion'] = rs[5]
                    obj['estado'] = rs[6]
                    obj['motivo_baja'] = rs[7]
                    obj['motivo_reincorporacion'] = rs[8]
                    obj['min_des'] = rs[9]
                    lista.append(obj)
        except conn.Error as e:
            app.logger.error(e)     
            obj = {}
            obj['codigo'] = e.pgcode
            obj['mensaje'] = e.pgerror            
        finally:
            if conn is not None:
                cur.close()
                conn.close()
        return lista

    def getListaComites(self):
        lista=[]
        querySQL = '''SELECT distinct(co.min_id), mi.min_des FROM membresia.comite_obreros co left join referenciales.ministerios mi on mi.min_id = co.min_id where co.estado is true and co.motivo_baja is null'''
        conexion = Conexion()
        conn = conexion.getConexion()
        cur = conn.cursor()
        try:
            cur.execute(querySQL)
            data = cur.fetchall()
            if len(data) > 0:
                for rs in data:
                    obj = {}
                    obj['min_id'] = rs[0]
                    obj['min_des'] = rs[1]
                    lista.append(obj)
        except conn.Error as e:
            app.logger.error(e)     
            obj = {}
            obj['codigo'] = e.pgcode
            obj['mensaje'] = e.pgerror            
        finally:
            if conn is not None:
                cur.close()
                conn.close()
        return lista