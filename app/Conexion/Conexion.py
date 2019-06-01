import psycopg2

class Conexion:

    # Se encapsula poniendo dos guiones bajos

    def __init__(self):
        """Método constructor de la clase Conexion.

        Mediante el método connect se obtiene una instancia de la
        conexion a la base de datos.

        """
        self.__con = psycopg2.connect("dbname=db_iglesia user=juandba host=localhost password=admin")

    def getConexion(self):
        """Método getConexion, retorna la conexion.

        Si la conexion se realizó en el método constructor de la Clase Conexion,
        se retorna dicha instancia.

        Retorna:
        con -- conexion

        """
        return self.__con  

    
        