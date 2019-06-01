from app.Conexion.Conexion import Conexion

class CiudadModel:

    def listarTodos(self):
        """Obtiene todas las ciudades.

        Obtiene todas las ciudades de la base de datos,
        mediante una consulta sencilla.

        Retorna:
        items -- tupla

        """
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cursor = con.cursor()
            cursor.execute("SELECT * FROM referenciales.ciudades")
            items = cursor.fetchall()        
            cursor.close()
            con.close()                
            return items
        except con.Error as e:
            print(e.pgerror)  

    def guardar(self, descripcion):
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cursor = con.cursor()
            cursor.execute("INSERT INTO ciudades(ciu_des) VALUES(UPPER(TRIM(%s)))",(descripcion,))
            con.commit()
            cursor.close()
            con.close()
            return True
        except con.Error as e:
            return e.pgerror
            
        
