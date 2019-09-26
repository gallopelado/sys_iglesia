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
