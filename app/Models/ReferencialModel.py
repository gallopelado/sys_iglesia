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


    def getReferencialJson(self, nombretabla):
        """getReferencialJson.

        Obtiene un json de los registros de una tabla que
        se encuentra en el esquema "referenciales".

        """

        sql = 'get_referencial_json'
        params = (nombretabla,)

        try:
            
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.callproc(sql, params)
            return cur.fetchall()[0][0]

        except con.Error as e:
            print(e.pgerror.encode('utf8'))
            return False
        finally:
            if con is not None:
                cur.close()
                con.close()
    
    def nuevoRegistro(self, esquema, tabla, valor):
        """Metodo nuevoRegistro
        
        Guarda un nuevo registro en una tabla simple.

        """
        # Obtener el segundo nombre de fila.        
        funcion = "public.insertone_referencial"
        parametros = (esquema, tabla, valor,)                       
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.callproc(funcion, parametros)            
            con.commit()
            return cur.fetchone()[0]
        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()                
                con.close()