from app.Conexion.Conexion import Conexion

class ContratoReservaModel:
    
    def obtenerContratosGenerados(self, anho):
        try:
            consulta = '''            
                select 
                    cr.res_id idreserva
                    , re.res_obs obs
                    , re.per_id idsolicitante
                    , soli.per_nombres solicitante_nombres
                    , soli.per_apellidos solicitante_apellidos	
                    , cr.encargado_id idencargado
                    , enca.per_nombres encargado_nombres
                    , enca.per_apellidos encargado_apellidos
                    , an.anho_des 
                from 
                    actividades.contrato_reserva cr
                left join actividades.reservas re using(res_id)
                left join referenciales.personas soli on re.per_id = soli.per_id 
                left join referenciales.personas enca on cr.encargado_id = enca.per_id
                left join referenciales.anho_habil an on re.anho_id = an.anho_id 
                where an.anho_des = %s  and re.res_estado = 'CONFIRMADO'              
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

    
    def obtenerContratoGeneradoId(self, id):
        try:
            consulta = '''            
                select 
                    cr.res_id idreserva
                    , re.res_obs obs
                    , re.per_id idsolicitante
                    , soli.per_nombres solicitante_nombres
                    , soli.per_apellidos solicitante_apellidos	
                    , cr.encargado_id idencargado
                    , enca.per_nombres encargado_nombres
                    , enca.per_apellidos encargado_apellidos
                    , TO_CHAR(cr.creacion_fecha,'DD "de" TMMonth "del" YYYY')fecha 
                    , cr.plantilla_contrato contrato
                from 
                    actividades.contrato_reserva cr
                left join actividades.reservas re using(res_id)
                left join referenciales.personas soli on re.per_id = soli.per_id 
                left join referenciales.personas enca on cr.encargado_id = enca.per_id
                left join referenciales.anho_habil an on re.anho_id = an.anho_id
                where cr.res_id = %s               
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
                    , ap.adp_nrocasa nrocasa	
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


    def obtenerPlantilla(self, id):
        try:
            consulta = '''                             
            select 
                con_id 
                , tcon_id 
                , tcon_des
                , con_titulo 
                , con_plantilla 
            from referenciales.contrato c
            left join referenciales.tipo_contrato using(tcon_id)
            where con_estado is true
            '''
            if id:
                consulta = consulta + ' AND con_id = %s'
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            if id:
                cur.execute(consulta, (id,))
                return cur.fetchone()
            cur.execute(consulta)                        
            return cur.fetchall()
        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()


    def obtenerEncargadoId(self, id):
        try:
            consulta = '''                             
            select array_to_json(array_agg(row_to_json(datos)))
                from (
                    select 
                        p.per_id id
                        , p.per_nombres nombres
                        , p.per_apellidos apellidos
                        , p.per_ci cedula
                        , adp.adp_direccion direccion
                        , adp.adp_nrocasa nrocasa
                    from referenciales.personas p
                    left join membresia.admision_persona adp on p.per_id=adp.adp_id
                    left join membresia.admision_adicionales adc on p.per_id= adc.add_id 
                    where p.is_propietario is true and p.per_id = %s
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


    def procesarContrato(self, resid, encargadoid, plantillacontrato, plantillatexto, creadoporusuario):
        try:
            consulta = 'actividades.generacion_contrato'
            parametros = (resid, encargadoid, plantillacontrato, plantillatexto, creadoporusuario,)            
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()            
            cur.callproc(consulta, parametros)
            con.commit()
            return cur.fetchone()[0]       
        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()