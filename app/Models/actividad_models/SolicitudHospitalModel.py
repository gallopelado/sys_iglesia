from app.Conexion.Conexion import Conexion

class SolicitudHospitalModel:
    def obtenerSolicitantes(self):
        querySQL = '''SELECT ap.adp_id idsolicitante, p.per_nombres nombres, p.per_apellidos apellidos
        FROM membresia.admision_persona ap 
        LEFT JOIN referenciales.personas p ON ap.adp_id = p.per_id 
        WHERE ap.adp_estado IS TRUE '''
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.execute(querySQL)
            return cur.fetchall()
        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()

    def obtenerPacientes(self):
        querySQL = '''SELECT per_id idpersona, per_nombres nombres, per_apellidos apellidos
        FROM referenciales.personas WHERE per_fechabaja is null'''
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.execute(querySQL)
            return cur.fetchall()
        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()

    def obtenerIdiomas(self):
        querySQL = 'SELECT * FROM referenciales.idiomas'
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.execute(querySQL)
            return cur.fetchall()
        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()

    def obtenerSolicitudesVoluntario(self):
        querySQL = '''select 
        vh.vh_id idsolicitud, vh.vh_des descripcion, vh.vh_estado from actividades.visi_hospi vh 
        where vh.vh_estado != 'CANCELADO'
        '''
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.execute(querySQL)
            return cur.fetchall()
        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()  

    def obtenerComitesActivos(self):
        querySQL = '''
        select 
            min_id idcomite
            , min_des
        from 
            membresia.comites c
        left join referenciales.ministerios using(min_id) 
        where com_estado is true
        '''
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.execute(querySQL)
            return cur.fetchall()
        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()           

    def obtenerIntegrantesComite(self, id):
        querySQL = '''
        select array_to_json(array_agg(row_to_json(datos))) from (
        select
            min_id idcomite ,
            min_des comite,
            per_id idpersona,
            per_nombres nombres,
            per_apellidos apellidos
        from
            membresia.comites c
        inner join membresia.comite_obreros using(min_id)
        left join referenciales.ministerios using(min_id)
        left join referenciales.personas using(per_id)
        where
            com_estado is true and min_id = %s)datos
        '''
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.execute(querySQL, (id, ))
            return cur.fetchone()[0]
        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()

    def obtenerSolicitudes(self, estado='NO-ATENDIDO'):
        querySQL = ''' 
        select array_to_json(array_agg(row_to_json(datos))) from (
        select 
            vh.vh_id idsolicitud
            , vh.vh_des descripcion
            , vh.solicitante_id idsolicitante
            , p.per_nombres nombres
            , p.per_apellidos apellidos
            , vh.vh_estado estado
        from actividades.visi_hospi vh 
        left join membresia.admision_persona ap on vh.solicitante_id = ap.adp_id
        left join referenciales.personas p on ap.adp_id = p.per_id
        where vh.vh_estado = %s ) datos
        '''
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            if (estado is not None or estado !='') and estado !='NO-ATENDIDO':
                cur.execute(querySQL, (estado,))
                return cur.fetchall()[0][0]
            cur.execute(querySQL, (estado,))
            return cur.fetchall()[0][0]
        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()

    def obtenerSolicitudId(self, id):
        querySQL = ''' 
        select 
            vh.vh_id idsolicitud	
            , vh.solicitante_id idsolicitante
            , vh.vh_des descripcion
            , vh.paciente_id idpaciente
            , vh.vh_estado estado
            , vh.vh_esmiembro esmiembro
            , vh.vh_estaenterado estaenterado 
            , vh.idi_id ididioma
            , vh.vh_nombrehospi nombrehospi 
            , vh.vh_nrocuarto nrocuarto
            , vh.vh_nrotelcuarto nrotelcuarto	
            , vh.vh_fechaadmi fechaadmi
            , vh.vh_diagnostico diagnostico
            , vh.vh_direhospi direhospi
            , vh.vh_horavisi horavisi
            , vh.vh_lunes lunes
            , vh.vh_martes martes
            , vh.vh_miercoles miercoles
            , vh.vh_jueves jueves
            , vh.vh_viernes viernes
            , vh.vh_sabado sabado
            , vh.vh_domingo domingo
        from actividades.visi_hospi vh 
        left join membresia.admision_persona ap on vh.solicitante_id = ap.adp_id
        left join referenciales.personas p on ap.adp_id = p.per_id 
        where vh.vh_id = %s
        '''
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()            
            cur.execute(querySQL, (id,))
            return cur.fetchone()
        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()

    def obtenerSolicitudIdJSON(self, id):
        querySQL = ''' 
        select array_to_json(array_agg(row_to_json(datos))) from (
        select 
            vh.vh_id idsolicitud	
            , vh.solicitante_id idsolicitante
            , vh.vh_des descripcion
            , vh.paciente_id idpaciente
            , vh.vh_estado estado
            , vh.vh_esmiembro esmiembro
            , vh.vh_estaenterado estaenterado 
            , vh.idi_id ididioma
            , vh.vh_nombrehospi nombrehospi 
            , vh.vh_nrocuarto nrocuarto
            , vh.vh_nrotelcuarto nrotelcuarto	
            , vh.vh_fechaadmi fechaadmi
            , vh.vh_diagnostico diagnostico
            , vh.vh_direhospi direhospi
            , vh.vh_horavisi horavisi
            , vh.vh_lunes lunes
            , vh.vh_martes martes
            , vh.vh_miercoles miercoles
            , vh.vh_jueves jueves
            , vh.vh_viernes viernes
            , vh.vh_sabado sabado
            , vh.vh_domingo domingo
        from actividades.visi_hospi vh 
        left join membresia.admision_persona ap on vh.solicitante_id = ap.adp_id
        left join referenciales.personas p on ap.adp_id = p.per_id 
        where vh.vh_id = %s)datos
        '''
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()            
            cur.execute(querySQL, (id,))
            return cur.fetchall()[0][0][0]
        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()

    def insertSolicitudHospital(self, solicitanteid, vhdes, pacienteid, vhesmiembro, vhestaenterado, 
        ididi, vhnombrehospi, vhnrocuarto, vhnrotelcuarto, vhfechaadmi, vhdiagnostico, 
        vhdirehospi, vhhoravisi, vhlunes, vhmartes, vhmiercoles, vhjueves, vhviernes, 
        vhsabado, vhdomingo, creadoporusuario, vhestado):
        insertSQL = '''
        INSERT INTO actividades.visi_hospi
        (solicitante_id, vh_des, paciente_id, vh_esmiembro, vh_estaenterado, 
        idi_id, vh_nombrehospi, vh_nrocuarto, vh_nrotelcuarto, vh_fechaadmi, vh_diagnostico, 
        vh_direhospi, vh_horavisi, vh_lunes, vh_martes, vh_miercoles, vh_jueves, vh_viernes, 
        vh_sabado, vh_domingo, creado_por_usuario, creacion_fecha, vh_estado)
        VALUES(%s, %s, %s, %s, %s, 
        %s, %s, %s, %s, %s, %s, 
        %s, %s, %s, %s, %s, %s, %s, 
        %s, %s, %s, now(), %s);
        '''
        parametros = (solicitanteid, vhdes, pacienteid, vhesmiembro, vhestaenterado, 
        ididi, vhnombrehospi, vhnrocuarto, vhnrotelcuarto, vhfechaadmi, vhdiagnostico, 
        vhdirehospi, vhhoravisi, vhlunes, vhmartes, vhmiercoles, vhjueves, vhviernes, 
        vhsabado, vhdomingo, creadoporusuario, vhestado,)
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

    def updateSolicitudHospital(self, solicitanteid, pacienteid, idiid, des, esmiembro, 
        estaenterado, nombrehospi, nrocuarto, nrotelcuarto, 
        fechaadmi, diagnostico, direhospi, horavisi, lunes, 
        martes, miercoles, jueves, viernes, sabado, 
        domingo, modificadoporusuario, idsolicitud):
        updateSQL = '''
        UPDATE actividades.visi_hospi
        SET solicitante_id=%s, paciente_id=%s, idi_id=%s, vh_des=%s, vh_esmiembro=%s, 
        vh_estaenterado=%s, vh_nombrehospi=%s, vh_nrocuarto=%s, vh_nrotelcuarto=%s, 
        vh_fechaadmi=%s, vh_diagnostico=%s, vh_direhospi=%s, vh_horavisi=%s, vh_lunes=%s, 
        vh_martes=%s, vh_miercoles=%s, vh_jueves=%s, vh_viernes=%s, vh_sabado=%s, 
        vh_domingo=%s, modificado_por_usuario=%s, modif_fecha=now()
        WHERE vh_id = %s;
        '''
        parametros = (solicitanteid, pacienteid, idiid, des, esmiembro, 
        estaenterado, nombrehospi, nrocuarto, nrotelcuarto, 
        fechaadmi, diagnostico, direhospi, horavisi, lunes, 
        martes, miercoles, jueves, viernes, sabado, 
        domingo, modificadoporusuario, idsolicitud,)
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

    def cancelaSolicitudHospital(self, idsolicitud):
        updateSQL = '''
        UPDATE actividades.visi_hospi
        SET vh_estado = 'CANCELADO', modificado_por_usuario = null, modif_fecha = now()
        WHERE vh_id = %s;
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

    def registrarListaSolicitudVoluntarios(self, id, fechavisita, horavisita, minid, 
    obs, creadoporusuario, voluntarios):
        insertSQL_cabecera = '''
        INSERT INTO actividades.lista_voluntario
        (vh_id, lvo_fechavisita, lvo_horavisita, min_id, lvo_obs, 
        creado_por_usuario, creacion_fecha)
        VALUES(%s, %s, %s, %s, %s, %s, now()) RETURNING lvo_id;
        '''
        insertSQL_detalle = '''
        INSERT INTO actividades.solicitud_lista_voluntario
        (lvo_id, per_id, estado)
        VALUES(%s, %s, %s);
        '''
        updateSQL_cabecera = '''
        UPDATE actividades.visi_hospi SET vh_estado = 'ATENDIDO', modificado_por_usuario = null, modif_fecha = NOW() WHERE vh_id = %s
        '''

        argumentos_cabecera = (id, fechavisita, horavisita, minid, 
        obs.upper(), creadoporusuario,)

        try:
            conexion = Conexion()
            con = conexion.getConexion()
            conexion.autocommit = False
            cur = con.cursor()
            ## Insertar cabecera
            cur.execute(insertSQL_cabecera, argumentos_cabecera)
            idlista = cur.fetchone()[0]
            if not idlista:
                print('No se inserto la cabecera')
                con.rollback()
                return False

            # Insertar detalle    
            for volun in voluntarios:
                cur.execute(insertSQL_detalle, (idlista, volun['value'], True))

            # Actualizar solicitud a ATENDIDO
            cur.execute(updateSQL_cabecera, (id,))

            con.commit()
            return True
        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()   

    def obtenerListasVoluntario(self):
        querySQL = ''' 
        select array_to_json(array_agg(row_to_json(datos))) from ( 
            SELECT 
                lvo_id idsolicitud
                , vh_des descripcion
                , fecha_formatolargo(lvo_fechavisita) fechavisita
                , vh_estado estado
            FROM actividades.lista_voluntario lv 
            left join actividades.visi_hospi using(vh_id)
            WHERE lvo_estado is not FALSE)datos
        '''
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()            
            cur.execute(querySQL)
            return cur.fetchall()[0][0]
        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()

    def obtenerListaVoluntarioId(self, id):
        querySQL = ''' 
        select array_to_json(array_agg(row_to_json(datos))) from (
        select 
            lvo_id idlista
            , vh_id idsolicitud
            , lvo_fechavisita fechavisita
            , lvo_horavisita horavisita
            , lvo_obs obs
            , min_id idcomite
        from actividades.lista_voluntario lv 
        where lvo_id = %s)datos
        '''
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()            
            cur.execute(querySQL, (id,))
            return cur.fetchone()[0][0]
        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()

    def eliminarVoluntario(self, idlista, idvoluntario):
        deleteSQL = ''' 
        DELETE FROM actividades.solicitud_lista_voluntario 
        WHERE lvo_id = %s AND per_id = %s
        '''
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()            
            cur.execute(deleteSQL, (idlista, idvoluntario,))
            con.commit()
            return True
        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()

    def agregarVoluntario(self, idlista, idvoluntario):
        insertSQL = ''' 
        INSERT INTO actividades.solicitud_lista_voluntario(lvo_id, per_id, estado) 
        VALUES (%s, %s, true)
        '''
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()            
            cur.execute(insertSQL, (idlista, idvoluntario,))
            con.commit()
            return True
        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()

    def actualizarListaVoluntario(self, vhid, lvofechavisita, lvohoravisita, lvoobs, modificadoporusuario):
        updateSQL = ''' 
        UPDATE actividades.lista_voluntario SET vh_id = %s,
        lvo_fechavisita = %s, lvo_horavisita = %s,
        lvo_obs = %s, modificado_por_usuario = %s,
        modif_fecha = NOW()
        '''
        updateSQL_visihospi = '''
        UPDATE actividades.visi_hospi SET vh_estado = 'ATENDIDO', modificado_por_usuario = null, modif_fecha = NOW() WHERE vh_id = %s
        '''
        parametros = (vhid, lvofechavisita, lvohoravisita, lvoobs, modificadoporusuario,)
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()            
            cur.execute(updateSQL, parametros)
            cur.execute(updateSQL_visihospi, (vhid,))
            con.commit()
            return True
        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()

    def obtenerVoluntariosRegistrados(self, id):
        querySQL = '''
        select array_to_json(array_agg(row_to_json(datos))) from (
        select 
            lvo_id idlista
            , per_id idvoluntario
            , per_nombres nombres
            , per_apellidos apellidos
        from actividades.solicitud_lista_voluntario slv
        left join referenciales.personas using(per_id)
        where lvo_id = %s
        )datos
        '''
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.execute(querySQL, (id, ))
            return cur.fetchone()[0]
        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()

    def eliminarListaVoluntario(self, id):
        updateSQL = '''
        UPDATE actividades.lista_voluntario
        SET lvo_estado = FALSE, modif_fecha = NOW()
        WHERE lvo_id = %s
        '''
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.execute(updateSQL, (id,))
            con.commit()
            return True
        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()

    def obtenerSolicitudesEstado(self, estado = 'ATENDIDO'):
        querySQL = '''
        select 
            lvo_id idlista
            , vh_id idsolicitud
            , vh_des observacion
            , vh_estado estado
            , min_id idcomite
            , com_des comite
        from actividades.lista_voluntario
        left join actividades.visi_hospi using(vh_id)
        left join membresia.comites using(min_id)
        where vh_estado = %s
        '''
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.execute(querySQL,(estado,))
            return cur.fetchall()
        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close() 

    def obtenerVoluntariosPorLista(self, id):
        querySQL = '''
        select array_to_json(array_agg(row_to_json(datos))) from (
        select 
            lvo_id idlista
            , per_id idvoluntario
            , per_nombres nombres
            , per_apellidos apellidos
        from actividades.solicitud_lista_voluntario slv 
        left join referenciales.personas using(per_id)
        where lvo_id = %s)datos
        '''
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.execute(querySQL,(id,))
            return cur.fetchall()[0][0]
        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()

    def insertInformeVisita(self, idlista, idvoluntario, descripcion, usuario):
        insertSQL = '''
        INSERT INTO actividades.informe_visi(lvo_id, per_id, descripcion,
        creado_por_usuario, creacion_fecha) VALUES (%s, %s, %s, %s, NOW())
        '''
        parametros = (idlista, idvoluntario, descripcion, usuario,)
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

    def updateInformeVisita(self, idlista, idvoluntario, descripcion, usuario):
        updateSQL = '''
        UPDATE actividades.informe_visi SET per_id = %s, descripcion = %s
        , modificado_por_usuario = %s, modif_fecha = NOW() WHERE lvo_id = %s
        '''
        parametros = (idvoluntario, descripcion, usuario, idlista,) 
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

    def obtenerInformes(self):
        querySQL = '''
        SELECT array_to_json(array_agg(row_to_json(datos))) FROM (
        select 
            lvo_id idlista
            , vh_des solicitud
            , per_id idvoluntario
            , per_nombres nombres
            , per_apellidos apellidos
        from actividades.informe_visi 
        left join actividades.lista_voluntario using(lvo_id)
        left join actividades.visi_hospi using(vh_id)
        left join referenciales.personas using(per_id))datos
        '''
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.execute(querySQL)
            return cur.fetchall()[0][0]
        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()

    def obtenerInformeId(self, id):
        querySQL = '''
        SELECT array_to_json(array_agg(row_to_json(datos))) FROM (
        select 
            lvo_id idlista
            , vh_des solicitud
            , per_id idvoluntario
            , per_nombres nombres
            , per_apellidos apellidos
            , descripcion 
            , vh_estado
            , com_des
        from actividades.informe_visi 
        left join actividades.lista_voluntario using(lvo_id)
        left join actividades.visi_hospi using(vh_id)
        left join membresia.comites using(min_id)
        left join referenciales.personas using(per_id) WHERE lvo_id = %s)datos
        '''
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.execute(querySQL, (id,))
            return cur.fetchone()[0][0]
        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()
