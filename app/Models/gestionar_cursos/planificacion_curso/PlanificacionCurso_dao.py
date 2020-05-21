from app.Conexion.Conexion import Conexion
class PlanificacionCurso_dao(Conexion):
    def __init__(self):
        Conexion.__init__(self)

    def getMaestros(self):
        lista_maestros = []
        querySQL = '''SELECT per_id,per_nombres, per_apellidos 
        FROM referenciales.maestros m 
        LEFT JOIN referenciales.personas USING(per_id)'''
        try:
            conn = self.getConexion()
            cur = conn.cursor()
            cur.execute(querySQL)
            data = cur.fetchall()
            for item in data:
                objeto = {}
                objeto['per_id'] = item[0]
                objeto['per_nombres'] = item[1]
                objeto['per_apellidos'] = item[2]
                lista_maestros.append(objeto)

        except conn.Error as e:
            print(e.pgerror)
        finally:
            if conn is not None:
                cur.close()
                conn.close()
        return lista_maestros