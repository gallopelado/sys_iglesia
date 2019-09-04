from app.Conexion.Conexion import Conexion
from app.Models.MiembroOficialModel import MiembroOficialModel

class MiembroPerfilModel():

    def listar(self):

        mo = MiembroOficialModel()
        return mo.listarMiembros()        

    
    def obtenerMiembroId(self, id):
        # SQL
        procedimiento = 'membresia.get_perfil_id'
        parametros = (id,)

        try:
            
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.callproc(procedimiento, parametros)
            return cur.fetchall()

        except con.Error as e:
            print(e.pgerror.encode('utf8'))
            return False
        finally:
            if con is not None:
                cur.close()
                con.close()

    
    def guardar(self, idmiembro, serviren, cualipers, 
    actiminis, anteced, estado, idusuario):

        # SQL
        procedimiento = 'membresia.alta_miembroperfil'
        parametros = (idmiembro, serviren, cualipers, actiminis, anteced,
        estado, idusuario,)
        try:
        
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.callproc(procedimiento, parametros)
            con.commit()
            res = cur.fetchone()[0]
            
            return res

        except con.Error as e:
            print(e.pgerror.encode('utf8'))
            return False
        finally:
            if con is not None:
                cur.close()
                con.close()
        
    

