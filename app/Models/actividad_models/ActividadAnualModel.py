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
        finally:
            if con is not None:
                cur.close()
                con.close()
