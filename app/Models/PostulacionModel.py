from app.Conexion.Conexion import Conexion

class PostulacionModel:

    def guardarNuevaPostulacion(self
            , minid
            ,postdes
            ,postdoc
            ,postestado
            ,postiniciopostu
            ,postfinpostu
            ,creadoporusuario
            ,detalle_idprofesion
            ,detalle_cantidad):
        '''Metodo guardarNuevaPostulacion.

            Se define el guardado de la postulacion con su detalle,
            retorna el id de dicho registro una vez persistido.

        '''

        # SQL
        procedimiento = 'membresia.nueva_postulacion'
        parametros = (int(minid), postdes, postdoc, postestado, postiniciopostu, postfinpostu, creadoporusuario, detalle_idprofesion,detalle_cantidad,)

        try:
            
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.callproc(procedimiento, parametros)
            con.commit()
            # Retorna el nombre del documento.
            return cur.fetchone()[0]

        except con.Error as e:
            print(e.pgerror)
            return False
        finally:
            if con is not None:
                cur.close()
                con.close()


    def traerPostulaciones(self):
        '''traerPostulaciones.

        Obtiene todas las postulaciones activas y sin fecha de procesado.

        '''

        procedimiento = 'membresia.getall_postulacion'

        try:
            
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.callproc(procedimiento)
            return cur.fetchall()
            
        except con.Error as e:
            print(e.pgerror)
            return False
        finally:
            if con is not None:
                cur.close()
                con.close()


    def traerPostulacionId(self, idpostulacion):
        '''traerPostulacionId.

        Obtiene la postulación según id sin restricción.

        '''
        
        procedimiento = 'membresia.get_postulacion_id'

        try:
            
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.callproc(procedimiento, (idpostulacion,))
            return cur.fetchone()

        except con.Error as e:
            print(e.pgerror)
            return False
        finally:
            if con is not None:
                cur.close()
                con.close()


    def reprogramar(self, opcion, idpostulacion, fechainicio=None, fechafin=None):
        '''reprogramar.

        Sirve para atrasar la fecha de postulacion siempre y cuando este activa.

        '''

        procedimiento = 'membresia.reprogramar_postulacion'
        parametros = (opcion, idpostulacion, fechainicio, fechafin, )

        try:
            
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.callproc(procedimiento, parametros)
            con.commit()            
            res = cur.fetchone()
            return res[0]

        except con.Error as e:            
            return e.pgcode
        finally:
            if con is not None:
                cur.close()
                con.close()


    def verificaVencimiento(self):
        '''verificaVencimiento.

        Verifica si la fecha de finalización coincide
        con la fecha actual, entoces cambia el estado del registro.

        '''
        procedimiento = 'CALL membresia.verifica_vecimiento_postulacion()'

        try:
            
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.execute(procedimiento)
            con.commit()
            print(con.notices)

        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()


    def anularPostulacion(self, idpostulacion):
        '''anularPostulacion.

        Si existe la postulación, cambia el estado a FALSE y agrega fecha de procesado.
        
        '''

        procedimiento = 'membresia.anular_postulacion'

        try:
        
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.callproc(procedimiento, (idpostulacion,))
            con.commit()
            return cur.fetchone()[0]

        except con.Error as e:
            print(e.pgerror)
            return False
        finally:
            if con is not None:
                cur.close()
                con.close()