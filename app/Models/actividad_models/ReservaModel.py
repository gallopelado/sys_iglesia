from app.Conexion.Conexion import Conexion


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
