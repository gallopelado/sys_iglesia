from app.Conexion.Conexion import Conexion

class ObreroModel:
    def traerPostulacionesProcesadas(self):
        consulta = '''
        SELECT post_id idpostulacion
        , post_des descripcion
        , to_char(post_fechacalificado, 'DD "de" TMMonth "del" YYYY') fechacalificado 
        FROM 
        membresia.cabe_postulacion 
        WHERE post_fechacalificado IS NOT null
        '''