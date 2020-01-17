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
