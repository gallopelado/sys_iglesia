from app.Conexion.Conexion import Conexion

class ContratoReservaModel:
    
    def obtenerReservasNoConfirmadas(self, anho):
        try:
            consulta = '''            
                select
                    res_id idreserva,                                        
                    res_obs obs                    
                from
                    actividades.reservas
                left join referenciales.anho_habil using(anho_id)
                where anho_des = %s  and res_estado = 'NO-CONFIRMADO'              
            '''
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.execute(consulta, (anho,))            
            return cur.fetchall()
        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()


    def obtenerEncargados(self):
        try:
            consulta = '''                             
            select
                per_id 
                , per_nombres
                , per_apellidos 
                , per_ci 
                , is_propietario 
            from referenciales.personas 
            where is_propietario is TRUE
            '''
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

    
    def obtenerDataReservaId(self, id):
        try:
            consulta = '''  
            select array_to_json(array_agg(row_to_json(datos)))
            from (          
                select 
                    r.res_id idreserva
                    , r.res_obs observacionreserva
                    , fecha_formatolargo(current_date)fechahoy
                    , p.per_id idpersona
                    , p.per_nombres nombres
                    , p.per_apellidos apellidos
                    , p.per_ci cedula
                    , ap.adp_direccion direccion 
                    , ap.adp_ecivil estadocivil
                    , ap.adp_email email
                    , fecha_formatolargo(ap.adp_fechanac) fechanacimiento
                    , adi.add_lugarnac lugarnacimiento	
                from actividades.reservas r
                left join referenciales.personas p on r.per_id = p.per_id
                left join membresia.admision_persona ap on p.per_id = ap.adp_id 
                left join membresia.admision_adicionales adi on p.per_id = adi.add_id
                WHERE r.res_id = %s 
            )datos              
            '''
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.execute(consulta, (id,))            
            return cur.fetchone()[0][0]
        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()