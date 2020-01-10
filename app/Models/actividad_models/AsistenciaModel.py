from app.Conexion.Conexion import Conexion

class AsistenciaModel:

    def procesar(self, opcion, asisid, eveid, asisdes, lista_personas, lista_asistio, lista_puntual):
        funcion = 'actividades.gestionar_asistencia'
        parametros = (opcion, asisid, eveid, asisdes, lista_personas, lista_asistio, lista_puntual,)
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


    def obtenerAsistencias(self, estado):
        consulta = '''
        select
            asis_id,
            eve_id,
            eve_des,
            asis_des descripcion,		
            asis_estado,	
            to_char(creacion_fecha, 'DD "de" TMMonth "del" YYYY')fecha	
        from
            actividades.cabe_asistencia
        left join referenciales.eventos using(eve_id)
        where asis_estado is %s
        '''        
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.execute(consulta, (estado,))            
            return cur.fetchall()
        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()

    