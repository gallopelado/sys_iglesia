from app.Conexion.Conexion import Conexion
from flask import current_app as app

class ReservaModel:

    def obtenerAnhoActivo(self):
        try:
            consulta = 'select anho_des from referenciales.anho_habil where is_active = true and adelantar = false'
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.execute(consulta)
            return cur.fetchall()[0][0]
        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()
    

    def obtenerSolicitantes(self):
        try:
            consulta = '''select ad.adp_id, p.per_nombres ||' '|| p.per_apellidos persona from membresia.admision_persona ad 
            left join referenciales.personas p on ad.adp_id = p.per_id
            where adp_estado is true'''
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

    def obtenerReservasJson(self, estado):
        try:
            consulta = '''
            select array_to_json(array_agg(row_to_json(datos)))
            from (
                select
                    res_id idreserva,
                    res_obs actividad,
                    fecha_formatolargo(res_fechainicio) fechainicio,
                    res_horainicio horainicio,		
                    res_estado estado
                from
                    actividades.reservas
                    where res_estado = %s
            )datos
            '''
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.execute(consulta, (estado,))            
            return cur.fetchone()[0]
        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()

    
    def obtenerReservaId(self, id):
        try:
            consulta = '''            
                select
                    res_id idreserva,
                    anho_des,
                    per_id idpersona,
                    eve_id idevento,
                    lug_id idlugar,	
                    res_fechainicio fechainicio,
                    res_horainicio horainicio,
                    res_fechafin fechafin,
                    res_horafin horafin,
                    res_obs obs,
                    res_estado
                from
                    actividades.reservas
                left join referenciales.anho_habil using(anho_id)
                where res_id = %s
            '''
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.execute(consulta, (id,))            
            return cur.fetchone()
        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()


    
    def guardarReserva(self, opcion, resid, anhoid, eveid, lugid, perid, 
    resfechainicio, reshorainicio, resfechafin, reshorafin, resobs, creadoporusuario, modificadoporusuario):
        parametros = (opcion, resid, anhoid, eveid, lugid, perid, 
        resfechainicio, reshorainicio, resfechafin, reshorafin, resobs, creadoporusuario, modificadoporusuario,)
        try:
            consulta = 'actividades.gestionar_reservas'
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.callproc(consulta, parametros)
            con.commit()  
            print(con.notices)                                            
            return True
        except con.Error as e:
            print(e.pgerror)            
            return e
        finally:
            if con is not None:
                cur.close()
                con.close()

    def getReservasByParameters(self, estado, fechadesde, fechahasta):
        lista=[]
        estados = ('CONFIRMADO', 'NO-CONFIRMADO', 'CANCELADO', 'DESACTIVADO')
        parametros = None
        querySQL = '''select
            r.res_id,
            r.anho_id,
            r.eve_id, e.eve_des, 
            r.lug_id, l.lug_des,
            r.per_id, concat(p.per_nombres, ' ', p.per_apellidos) persona,
            fecha_formatolargo(r.res_fechainicio) fechainicio,
            r.res_horainicio,
            fecha_formatolargo(r.res_fechafin) fechafin,
            r.res_horafin,
            r.res_obs,
            r.res_estado
        from
            actividades.reservas r
        left join referenciales.eventos e on e.eve_id = r.eve_id 
        left join referenciales.lugares l on l.lug_id = r.lug_id 
        left join referenciales.personas p on p.per_id = r.per_id'''
        if estado=='CUALQUIER' and not fechadesde and not fechahasta:#Only estado
            querySQL += ''
        elif estado != 'CUALQUIER' and estado in estados and not fechadesde and not fechahasta:#Only estado distinct anybody
            querySQL += ' WHERE r.res_estado = %s'
            parametros = (estado,)
        elif estado != 'CUALQUIER' and estado in estados and fechadesde and fechahasta:#ideal case
            querySQL += ' WHERE r.res_estado = %s AND r.res_fechainicio BETWEEN %s AND %s'
            parametros = (estado, fechadesde, fechahasta,)
        conexion = Conexion()
        conn = conexion.getConexion()
        cur = conn.cursor()
        try:
            if parametros:
                cur.execute(querySQL, parametros)
            else:
                cur.execute(querySQL)
            data = cur.fetchall()
            if len(data) > 0:
                for rs in data:
                    obj = {}
                    obj['res_id'] = rs[0]
                    obj['anho_id'] = rs[1]
                    obj['eve_id'] = rs[2]
                    obj['eve_des'] = rs[3]
                    obj['lug_id'] = rs[4]
                    obj['lug_des'] = rs[5]
                    obj['per_id'] = rs[6]
                    obj['persona'] = rs[7]
                    obj['fechainicio'] = rs[8]
                    obj['res_horainicio'] = rs[9]
                    obj['fechafin'] = rs[10]
                    obj['res_horafin'] = rs[11]
                    obj['res_obs'] = rs[12]
                    obj['res_estado'] = rs[13]
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
