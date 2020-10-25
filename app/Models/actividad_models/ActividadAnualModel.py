from app.Conexion.Conexion import Conexion
from flask import current_app as app

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

    
    def obtenerActividadesId(self, id):
        try:
            consulta = '''            
                select
                    act_id idactividad,
                    anho_des anho,
                    eve_id,
                    min_id,
                    lug_id,                    
                    act_fechainicio,
                    act_horainicio,
                    act_fechafin,
                    act_horafin,
                    plaz_id,
                    act_repite,
                    act_obs                    	
                from
                    actividades.actividades
                lef join referenciales.anho_habil using(anho_id)
                where act_id = %s
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

    
    def guardarActividad(self, opcion, id, anhohabil, eveid, lugid, fechaini, horaini, fechafin, horafin,
	plazid, actrepite, actobs, minid, creadoporusuario):
        parametros = (opcion, id, anhohabil, eveid, lugid, fechaini, horaini, fechafin, horafin,
	                plazid, actrepite, actobs, minid, creadoporusuario,)
        try:
            consulta = '''CALL actividades.gestionar_actividades_anuales(
                %s,--opcion character varying,
                %s,--id integer,
                %s,--anhohabil integer,
                %s,--eveid integer,
                %s,--lugid integer,
                %s,--fechaini date,
                %s,--horaini time without time zone,
                %s,--fechafin date,
                %s,--horafin time without time zone,
                %s,--plazid integer,
                %s,--actrepite boolean,
                %s,--actobs text,
                %s,--minid integer,
                %s)--creadoporusuario integer)'''
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.execute(consulta, parametros)
            con.commit()  
            print(con.notices)                                            
            return True
        except con.Error as e:
            print(e.pgerror)
            #print(e.args[0])
            return e
        finally:
            if con is not None:
                cur.close()
                con.close()

    def getListaActividadesAnhoActivo(self, min_id, lug_id, fechadesde, fechahasta):
        lista=[]
        querySQL = '''SELECT 
            ac.act_id, ac.anho_id, ac.eve_id, e.eve_des
            , ac.lug_id, lu.lug_des
            , fecha_formatolargo(ac.act_fechainicio) fechainicio, ac.act_horainicio
            , fecha_formatolargo(ac.act_fechafin) fechafin, ac.act_horafin
            , ac.plaz_id, ac.act_repite, ac.act_obs, ac.min_id, m.min_des
        FROM actividades.actividades ac
        left join referenciales.eventos e on e.eve_id = ac.eve_id
        left join referenciales.lugares lu on lu.lug_id = ac.lug_id
        left join referenciales.ministerios m on m.min_id = ac.min_id
        where ac.anho_id = (select anho_id from referenciales.anho_habil where is_active is true and adelantar is false)
        '''
        parameters = None
        if not min_id and not lug_id and not fechadesde and not fechahasta:#Without parameters, simple query
            querySQL += ''''''
        elif min_id and not lug_id and not fechadesde and not fechahasta:#only evento
            querySQL += ''' and ac.min_id=%s'''
            parameters = (min_id,)
        elif not min_id and lug_id and not fechadesde and not fechahasta:#only lugar
            querySQL += ''' and ac.lug_id=%s'''
            parameters = (lug_id,)
        elif min_id and lug_id and not fechadesde and not fechahasta:#only evento, lugar
            querySQL += ''' and ac.min_id=%s and ac.lug_id=%s'''
            parameters = (lug_id,)
        elif min_id and lug_id and fechadesde and fechahasta:#ideal case
            querySQL += ''' and ac.min_id=%s and ac.lug_id=%s and ac.act_fechainicio BETWEEN %s and %s'''
            parameters = (min_id, lug_id, fechadesde, fechahasta,)
        elif not min_id and not lug_id and fechadesde and fechahasta:#only date
            querySQL += ''' and ac.act_fechainicio BETWEEN %s and %s'''
            parameters = (fechadesde, fechahasta,)
        conexion = Conexion()
        conn = conexion.getConexion()
        cur = conn.cursor()
        try:
            if parameters:
                cur.execute(querySQL, parameters)
            else:
                cur.execute(querySQL)
            data = cur.fetchall()
            if len(data) > 0:
                for rs in data:
                    obj = {}
                    obj['act_id'] = rs[0]
                    obj['anho_id'] = rs[1]
                    obj['eve_id'] = rs[2]
                    obj['eve_des'] = rs[3]
                    obj['lug_id'] = rs[4]
                    obj['lug_des'] = rs[5]
                    obj['fechainicio'] = rs[6]
                    obj['act_horainicio'] = rs[7]
                    obj['fechafin'] = rs[8]
                    obj['act_horafin'] = rs[9]
                    obj['plaz_id'] = rs[10]
                    obj['act_repite'] = rs[11]
                    obj['act_obs'] = rs[12]
                    obj['min_id'] = rs[13]
                    obj['min_des'] = rs[14]
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

    def getOrganizadores(self):
        lista=[]
        querySQL = '''SELECT DISTINCT(ac.min_id), m.min_des FROM actividades.actividades ac left join referenciales.ministerios m on m.min_id = ac.min_id where ac.anho_id = (select anho_id from referenciales.anho_habil where is_active is true and adelantar is false)'''
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

    def getLugares(self):
        lista=[]
        querySQL = '''SELECT DISTINCT(ac.lug_id), lu.lug_des FROM actividades.actividades ac left join referenciales.eventos e on e.eve_id = ac.eve_id left join referenciales.lugares lu on lu.lug_id = ac.lug_id where ac.anho_id = (select anho_id from referenciales.anho_habil where is_active is true and adelantar is false)'''
        conexion = Conexion()
        conn = conexion.getConexion()
        cur = conn.cursor()
        try:
            cur.execute(querySQL)
            data = cur.fetchall()
            if len(data) > 0:
                for rs in data:
                    obj = {}
                    obj['lug_id'] = rs[0]
                    obj['lug_des'] = rs[1]
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
