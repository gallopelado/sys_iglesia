from app.Conexion.Conexion import Conexion
from app.Models.MiembroOficialModel import MiembroOficialModel

class MiembroPerfilModel():

    def listar(self):

        mo = MiembroOficialModel()
        return mo.listarMiembros()        

    def guardar(self, id, serviren, cualipers, 
    actiminis, anteced, estado, idusuario):

        # SQL
        procedimiento = 'membresia.altamiembroperfil'
        parametros = (id, serviren, cualipers, actiminis, anteced,
        estado, idusuario,)
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
        
    ## (2, 'tesoreria', 'buen tipo', 'buen administrador', null,
	##now(), true, null): : membresia.miembro_perfil

