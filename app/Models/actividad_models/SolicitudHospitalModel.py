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
            return cur.fetchone()
        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()    