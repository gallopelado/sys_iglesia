from app.Conexion.Conexion import Conexion
class ConsejeriaModel:
    def getMiembros(self):
        selectSQL = '''
        select array_to_json(array_agg(row_to_json(datos) ) ) from ( 
            select 
                ap.adp_id idmiembro
                , p.per_nombres ||' '|| p.per_apellidos miembro
                , extract(years from age(current_timestamp, ap.adp_fechanac::timestamp)) edad
                , ap.adp_ecivil ecivil
                , ap.conyuge_id idconyuge
                , p2.per_nombres ||' '||p2.per_apellidos conyuge
                , extract(years from age(current_timestamp, ad2.adp_fechanac::timestamp)) edadconyuge 
                , extract(years from age(current_timestamp, ap.adp_fechamatri::timestamp))||' años'::varchar tiempocasado
            from membresia.admision_persona ap
            inner join membresia.admision_adicionales ad on ad.add_id = ap.adp_id 
            inner join referenciales.personas p on p.per_id = ap.adp_id 
            left join referenciales.personas p2 on p2.per_id = ap.conyuge_id 
            left join membresia.admision_persona ad2 on ad2.adp_id = ap.conyuge_id 
            where ap.adp_estado is true
            order by p.per_nombres asc)datos
        '''
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.execute(selectSQL)
            return cur.fetchone()[0]
        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()

    def getConsejeros(self):
        selectSQL = '''
        select array_to_json(array_agg(row_to_json(datos) ) ) from ( 
            select 
                per_id idconsejero
                , per_nombres||' '||per_apellidos consejero
            from membresia.comite_obreros co  
            inner join referenciales.personas using(per_id)
            where min_id = 9 -- 9 es consejeria en la BD
            order by per_nombres asc
           )datos
        '''
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.execute(selectSQL)
            return cur.fetchone()[0]
        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()