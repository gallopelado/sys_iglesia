from app.Conexion.Conexion import Conexion

class ListaCandidatoModel:

    def traerPostulaciones(self, opcion):

        funcion = 'membresia.get_postulaciones'

        try:
            
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.callproc(funcion, (opcion, ))
            return cur.fetchall()

        except con.Error as e:
            print(e.pgerror)
            return False
        finally:
            if con is not None:
                cur.close()
                con.close()


    def traerListaCandidatos(self, idpostulacion):

        funcion = 'membresia.get_listapostulantes_id'

        try:
            
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.callproc(funcion, (idpostulacion,))
            res = cur.fetchone()
            return res

        except con.Error as e:
            print(e.pgerror)
            return True
        finally:
            if con is not None:
                cur.close()
                con.close()

    
    def traerDetalleCandidatos(self, idpostulacion):

        consultaSQL = 'SELECT detalle FROM membresia.get_listapostulantes_id(%s)'

        try:
            
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.execute(consultaSQL, (idpostulacion, ))
            res = cur.fetchone()[0]
            return res

        except con.Error as e:
            print(e.pgerror)
            return False
        finally:
            if con is not None:
                cur.close()
                con.close()


    def eliminarCandidato(self, idpostulacion, idcandidato):

        consultaSQL = 'DELETE FROM membresia.candi_detalle WHERE post_id = %s AND mo_id = %s'

        try:
            
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.execute(consultaSQL, (idpostulacion, idcandidato,))
            con.commit()
            return True

        except con.Error as e:
            print(e.pgerror)
            return False
        finally:
            if con is not None:
                cur.close()
                con.close()


    def guardarLista(self, idpostulacion, lista):
         
         procedimiento = 'CALL membresia.nueva_lista_candidatos(%s, %s)'

         try:
             
             conexion = Conexion()
             con = conexion.getConexion()
             cur = con.cursor()
             cur.execute(procedimiento, (idpostulacion, lista,))
             con.commit()
             return True

         except con.Error as e:
             print(e.pgerror)
             return False
         finally:
             if con is not None:
                 cur.close()
                 con.close()
    