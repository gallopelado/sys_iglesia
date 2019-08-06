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
            print(e.pgerror.encode('utf8'))
            return False
        finally:
            if con is not None:
                cur.close()
                con.close()
