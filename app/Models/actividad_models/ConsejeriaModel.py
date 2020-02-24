from app.Conexion.Conexion import Conexion
class ConsejeriaModel:
    def getMiembros(self):
        selectSQL = '''
        select array_to_json(array_agg(row_to_json(datos) ) ) from ( 
            select 
                ap.adp_id idmiembro
                , p.per_nombres ||' '|| p.per_apellidos miembro
                , extract(years from age(current_timestamp, ap.adp_fechanac::timestamp)) edad
                , ap.adp_ecivil ecivil
                , ap.conyuge_id idconyuge
                , p2.per_nombres ||' '||p2.per_apellidos conyuge
                , extract(years from age(current_timestamp, ad2.adp_fechanac::timestamp)) edadconyuge 
                , extract(years from age(current_timestamp, ap.adp_fechamatri::timestamp))||' años'::varchar tiempocasado
            from membresia.admision_persona ap
            inner join membresia.admision_adicionales ad on ad.add_id = ap.adp_id 
            inner join referenciales.personas p on p.per_id = ap.adp_id 
            left join referenciales.personas p2 on p2.per_id = ap.conyuge_id 
            left join membresia.admision_persona ad2 on ad2.adp_id = ap.conyuge_id 
            where ap.adp_estado is true
            order by p.per_nombres asc)datos
        '''
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.execute(selectSQL)
            return cur.fetchone()[0]
        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()

    def getMiembroId(self, id):
        selectSQL = '''
        select array_to_json(array_agg(row_to_json(datos) ) ) from ( 
            select 
                ap.adp_id idmiembro
                , p.per_nombres ||' '|| p.per_apellidos miembro
                , extract(years from age(current_timestamp, ap.adp_fechanac::timestamp)) edad
                , ap.adp_ecivil ecivil
                , ap.conyuge_id idconyuge
                , p2.per_nombres ||' '||p2.per_apellidos conyuge
                , extract(years from age(current_timestamp, ad2.adp_fechanac::timestamp)) edadconyuge 
                , extract(years from age(current_timestamp, ap.adp_fechamatri::timestamp))||' años'::varchar tiempocasado
            from membresia.admision_persona ap
            inner join membresia.admision_adicionales ad on ad.add_id = ap.adp_id 
            inner join referenciales.personas p on p.per_id = ap.adp_id 
            left join referenciales.personas p2 on p2.per_id = ap.conyuge_id 
            left join membresia.admision_persona ad2 on ad2.adp_id = ap.conyuge_id 
            where ap.adp_estado is true and ap.adp_id = %s 
            order by p.per_nombres asc)datos
        '''
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.execute(selectSQL, (id,))
            return cur.fetchone()[0]
        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()

    def getSolicitudes(self):
        selectSQL = '''
        select array_to_json(array_agg(row_to_json(datos) ) ) from ( 
            select
                cons_id idsolicitud
                , per_id idsolicitante
                , per_nombres||' '||per_apellidos solicitante
                , TO_CHAR(creacion_fecha ,'DD "de" TMMonth "del" YYYY')fecha
                , cons_estado estado
            from actividades.solicitud_consejeria sc
            left join referenciales.personas using(per_id)
            where cons_estado != 'CANCELADO'
            order by per_nombres
            )datos
        '''
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.execute(selectSQL, (id,))
            return cur.fetchall()[0][0]
        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()

    def getSolicitudId(self, id):
        selectSQL = '''
        select array_to_json(array_agg(row_to_json(datos) ) ) from ( 
            select
                sc.cons_id idsolicitud
                , sc.per_id idsolicitante
                , p.per_nombres||' '||p.per_apellidos solicitante
                , extract(years from age(current_timestamp, ap.adp_fechanac::timestamp)) edad
                , ap.adp_ecivil ecivil
                , ap.conyuge_id idconyuge
                , p2.per_nombres ||' '|| p2.per_apellidos conyuge
                , extract(years from age(current_timestamp, ap2.adp_fechanac::timestamp)) edadconyuge 
                , extract(years from age(current_timestamp, ap.adp_fechamatri::timestamp))||' años'::varchar tiempocasado
                , sc.reli_id idreligion
                , r.reli_des religion
                , sc.cons_servcentral servcentral
                , sc.cons_gruposcrecimiento gruposcrecimiento
                , sc.cons_servsemana servsemana
                , sc.cons_descrmatriant descrmatriant
                , sc.cons_hijos descr_hijos
                , sc.gcre_id idgrupo
                , g.gcre_des grupo
                , sc.cons_consultado consultogrupo
                , sc.cons_conversion convertido
                , sc.cons_asesoria asesoria
                , sc.consejero_id idconsejero
                , p3.per_nombres ||' '||p3.per_apellidos consejero
            from actividades.solicitud_consejeria sc
            left join membresia.admision_persona ap on ap.adp_id = sc.per_id
            left join referenciales.personas p on  p.per_id = sc.per_id 
            left join referenciales.personas p2 on p2.per_id = ap.conyuge_id 
            left join membresia.admision_persona ap2 on ap2.adp_id = ap.conyuge_id
            left join referenciales.religion r on r.reli_id = sc.reli_id 
            left join referenciales.grupo_crecimiento g on g.gcre_id = sc.gcre_id 
            left join referenciales.personas p3 on p3.per_id = sc.consejero_id 
            WHERE sc.cons_id = %s
            )datos
        '''
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.execute(selectSQL, (id,))
            return cur.fetchone()[0][0]
        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()

    def getConsejeros(self):
        selectSQL = '''
        select array_to_json(array_agg(row_to_json(datos) ) ) from ( 
            select 
                per_id idconsejero
                , per_nombres||' '||per_apellidos consejero
            from membresia.comite_obreros co  
            inner join referenciales.personas using(per_id)
            where min_id = 9 -- 9 es consejeria en la BD
            order by per_nombres asc
           )datos
        '''
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.execute(selectSQL)
            return cur.fetchone()[0]
        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()

    def insertSolicitud(self, perid, reliid, consejeroid, gcreid, consservcentral, consgruposcrecimiento, consservsemana, 
        consdescrmatriant, conshijos, consconsultado, consconversion, consasesoria, 
        consestado, creadoporusuario, creacionfecha):
        insertSQL = '''
        INSERT INTO actividades.solicitud_consejeria
        (per_id, reli_id, consejero_id, gcre_id, cons_servcentral, cons_gruposcrecimiento, cons_servsemana, 
        cons_descrmatriant, cons_hijos, cons_consultado, cons_conversion, cons_asesoria, 
        cons_estado, creado_por_usuario, creacion_fecha)
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 'ATENDIDO', null, now());
        '''
        parametros = (perid, reliid, consejeroid, gcreid, consservcentral, consgruposcrecimiento,consservsemana, 
        consdescrmatriant, conshijos, consconsultado, consconversion, consasesoria,)
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.execute(insertSQL, parametros)
            con.commit()
            return True
        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()

    def updateSolicitud(self, idsolicitud, perid, reliid, consejeroid, gcreid, consservcentral, consgruposcrecimiento, consservsemana, 
        consdescrmatriant, conshijos, consconsultado, consconversion, consasesoria, 
        consestado, modificadoporusuario, modiffecha):
        updateSQL = '''
        UPDATE actividades.solicitud_consejeria
        SET per_id=%s, reli_id=%s, consejero_id=%s, gcre_id=%s, cons_servcentral=%s, cons_gruposcrecimiento=%s,
        cons_servsemana=%s, cons_descrmatriant=%s, cons_hijos=%s, cons_consultado=%s, cons_conversion=%s, cons_asesoria=%s, modificado_por_usuario=null, modif_fecha=now()
        WHERE cons_id=%s;

        '''
        parametros = (perid, reliid, consejeroid, gcreid, consservcentral, consgruposcrecimiento,consservsemana, 
        consdescrmatriant, conshijos, consconsultado, consconversion, consasesoria, idsolicitud,)
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.execute(updateSQL, parametros)
            con.commit()
            return True
        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()

    def cancelaSolicitud(self, idsolicitud):
        updateSQL = '''
        UPDATE actividades.solicitud_consejeria
        SET cons_estado = 'CANCELADO', modificado_por_usuario=null, modif_fecha=now()
        WHERE cons_id=%s;
        '''        
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.execute(updateSQL, (idsolicitud,))
            con.commit()
            return True
        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()