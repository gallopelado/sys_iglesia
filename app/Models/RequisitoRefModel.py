from app.Conexion.Conexion import Conexion

class RequisitoRefModel():
    """Clase RequisitoRefModel.
    Se definen los metodos de acceso y gestion de datos a la BD
    del referencial requisitos.

    """
    def getAllRequisitosJson(self):
        #SQL
        procedimiento = 'referenciales.obtener_todos_requisitos_json'
        
        try:
            
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.callproc(procedimiento)
            return cur.fetchone()

        except con.Error as e:
            print(str(e.pgerror).encode('utf-8'))
            return False
        finally:
            if con is not None:
                cur.close()
                con.close()
