from app.Conexion.Conexion import Conexion

class MiembroOficialModel():
    
    def guardar(self, id, razonaltaid, fechaconversion, fechabautismo,
                lugarbautismo, oficiador, fechainiciomembresia, estadomembresia, 
                bautizadoeniglesia, padresmiembros, recibioes, obs,
                creadoporusuario):
        
        # SQL
        procedimiento = 'membresia.alta_miembrooficial'
        parametros = (id, razonaltaid, fechaconversion, fechabautismo,
                      lugarbautismo, oficiador, fechainiciomembresia, estadomembresia,
                      bautizadoeniglesia, padresmiembros, recibioes, obs,
                      creadoporusuario, )
        
        try:
            
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.callproc(procedimiento, parametros)
            con.commit()
            return cur.fetchone()

        except con.Error as e:
            print(e.pgerror)
            return False
        finally:
            if con is not None:
                cur.close()
                con.close()

                
    def modificar(self, id, razonaltaid, fechaconversion, fechabautismo,
                lugarbautismo, oficiador, fechainiciomembresia, estadomembresia,
                bautizadoeniglesia, padresmiembros, recibioes, obs,
                creadoporusuario):

        # SQL
        procedimiento = 'membresia.modificar_miembrooficial'
        parametros = (id, razonaltaid, fechaconversion, fechabautismo,
                      lugarbautismo, oficiador, fechainiciomembresia, estadomembresia,
                      bautizadoeniglesia, padresmiembros, recibioes, obs,
                      creadoporusuario, )

        try:

            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.callproc(procedimiento, parametros)
            con.commit()
            return cur.fetchone()

        except con.Error as e:
            print(e.pgerror)
            return False
        finally:
            if con is not None:
                cur.close()
                con.close()


    def listarMiembros(self):

        funcion = 'membresia.get_miembros_vistaprincipal'

        try:
            
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.callproc(funcion)
            return cur.fetchall()

        except con.Error as e:
            print(e.pgerror.encode('utf8'))
            return False
        finally:
            if con is not None:
                cur.close()
                con.close()


    def getMiembroById(self, idmiembro):

        funcion = 'membresia.get_miembrosoficiales_by_id'

        try:
            
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.callproc(funcion, (idmiembro,))
            return cur.fetchone()

        except con.Error as e:
            print(e.pgerror.encode('utf8'))
            return False
        finally:
            if con is not None:
                cur.close()
                con.close()
    

    def getMiembrosDadosDeBaja(self):

        procedimiento = 'membresia.get_miembros_baja'

        try:
            
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.callproc(procedimiento)
            return cur.fetchall()

        except con.Error as e:
            print(e.pgerror.encode('utf8'))
            return False
        finally:
            if con is not None:
                cur.close()
                con.close()


    def reincorporarMiembro(self, idmiembro, obs):

        procedimiento = 'membresia.reincorporar_miembro'

        try:
            
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.callproc(procedimiento, (idmiembro, obs,))
            con.commit()
            return cur.fetchone()

        except con.Error as e:
            print(e.pgerror.encode('utf8'))
            return False
        finally:
            if con is not None:
                cur.close()
                con.close()


    def listarTodosMiembros(self):
        funcion = 'membresia.get_miembro_admision'
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.callproc(funcion)
            return cur.fetchone()
        except con.Error as e:
            print(e.pgerror)
            return False
        finally:
            if con is not None:
                cur.close()
                con.close()