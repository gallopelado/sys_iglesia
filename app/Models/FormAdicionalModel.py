from app.Conexion.Conexion import Conexion


class FormAdicionalModel():

    def listarFormularios(self):
        """"Metodo listarFormularios.

        Se define una consulta en la BD que obtiene aquellos
        formularios con estado activo.

        """

        consulta = """ 
        
            SELECT a.add_id,
            p.per_nombres||' '||p.per_apellidos persona, p.per_ci cedula 
            FROM membresia.admision_adicionales a 
            inner join referenciales.personas p on a.add_id = p.per_id
            where add_estado <> false;
        
        """

        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()

            cur.execute(consulta)

            return cur.fetchall()

        except con.Error as e:
            
            print(e.pgerror)
            return False

        finally:
            if con is not None:
                cur.close()
                con.close()
