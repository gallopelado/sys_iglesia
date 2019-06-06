# Se importa la Clase Conexion
from app.Conexion.Conexion import Conexion

class CiudadModel:
    """Clase CiudadModel.

    Esta clase contiene metodos para gestionar acciones del modelo Ciudad en la
    base de datos.

    Autor: Juan Jose Gonzalez Ramirez <juanftp100@gmail.com>

    """
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
        """Guarda registro de ciudad.

        Este metodo se encarga de guardar ciudad en la
        base de datos.

        Retorna: 
        True o Mensaje de error.

        """
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cursor = con.cursor()
            cursor.execute("INSERT INTO referenciales.ciudades(ciu_des) VALUES(UPPER(TRIM(%s)))",(descripcion,))
            con.commit()
            cursor.close()
            con.close()
            return True
        except con.Error as e:
            return e.pgerror

    def modificar(self, idciudad, descripcion):
        """Modificar registro de ciudad.

        Este metodo se encarga de modificar el registro de ciudad en la base de datos.

        Retorna: 
        True o Mensaje de error.

        """
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cursor = con.cursor()
            cursor.execute("""
            UPDATE referenciales.ciudades SET ciu_des = UPPER(%s) 
            WHERE ciu_id = %s;
            """, (descripcion, idciudad))  
            con.commit()   
            cursor.close()
            con.close()
            return True
        except con.Error as e:
            return e.pgerror  
            
    def recuperaCiudad(self, idciudad):

        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cursor = con.cursor()
            cursor.execute("""
            SELECT ciu_id id, ciu_des descripcion FROM referenciales.ciudades 
            WHERE ciu_id = %s;
            """, (idciudad))
            item = cursor.fetchone()
            cursor.close()
            con.close()            
            return item
        except con.Error as e:
            return e.pgerror        

    def eliminar(self, idciudad):

        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cursor = con.cursor()
            cursor.execute("""
            DELETE FROM referenciales.ciudades WHERE ciu_id = %s
            """, (idciudad))
            con.commit()
            cursor.close()
            con.commit()
            return True
        except con.Error as e:
            return e.pgerror