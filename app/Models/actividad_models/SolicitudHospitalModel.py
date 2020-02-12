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
            return cur.fetchall()[0]
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