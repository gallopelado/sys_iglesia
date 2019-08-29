from app.Conexion.Conexion import Conexion

class ReferencialModel():

    def getAll(self, nombretabla):

        procedimiento = 'getall_referencial'
        parametros = (nombretabla,)

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