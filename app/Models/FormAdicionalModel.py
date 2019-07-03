from app.Conexion.Conexion import Conexion


class FormAdicionalModel():

    def listarFormularios(self):
        """"Metodo listarFormularios.

        Se define una consulta en la BD que obtiene aquellos
        formularios con estado activo.

        """

        consulta = """ 
        
            SELECT 
                a.add_id,
                p.per_nombres||' '||p.per_apellidos persona, p.per_ci cedula, (SELECT to_char(a.fecha_modificado, 'DD/MM/YYYY'::TEXT)) 
            FROM 
                membresia.admision_adicionales a 
            inner join referenciales.personas p 
                on a.add_id = p.per_id
            where 
                add_estado <> false;
        
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

    def obtenerDatosId(self, idadi):
        """Metodo obtenerDatosId.

        Se define la obtencion de los datos del formulario de datos adicionales
        de la base de datos, retorna una lista.

        """

        # SQL
        consulta1 = """
        SELECT adi.add_id, 
        p.per_nombres||' '||p.per_apellidos persona,
        adi.nac_id, adi.add_lugarnac, adi.san_id, adi.add_alergias, adi.add_capacdife, adi.add_foto, adi.add_estado
        FROM membresia.admision_adicionales adi
        left join referenciales.personas p on adi.add_id = p.per_id
        where adi.add_id = %s AND adi.add_estado <> false;
        """

        try:

            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.execute(consulta1, (idadi, ))

            return cur.fetchone()

        except con.Error as e:
            print(e.pgerror)
            return False
        finally:
            if con is not None:
                cur.close()
                con.close()
    
    def obtenerDatosIdJSON(self, idadi):
        """Metodo obtenerDatosId.

        Se define la obtencion de los datos del formulario de datos adicionales
        de la base de datos, retorna una lista.

        """

        # SQL
        consulta1 = """
        SELECT 
            ARRAY_TO_JSON(ARRAY_AGG(ROW_TO_JSON(data)))
        FROM (
            SELECT adi.add_id idadicional, 
                p.per_nombres||' '||p.per_apellidos persona,
                adi.nac_id idnacionalidad,
                nac.nac_des nacionalidad, 
                adi.add_lugarnac lugarnacimiento, 
                adi.san_id idtiposangre,
                san.san_des sangre,
                adi.add_alergias alergias,
                adi.add_capacdife capacidades,
                adi.add_foto foto,
                adi.add_estado estado
            FROM 
                membresia.admision_adicionales adi
            LEFT JOIN referenciales.personas p ON 
                adi.add_id = p.per_id
            LEFT JOIN referenciales.nacionalidad nac ON
                adi.nac_id = nac.nac_id
            LEFT JOIN referenciales.sangre san ON
                adi.san_id = san.san_id
            WHERE 
                adi.add_id = %s AND adi.add_estado <> false) data;
        """

        try:

            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.execute(consulta1, (idadi, ))

            return cur.fetchone()

        except con.Error as e:
            print(e.pgerror)
            return False
        finally:
            if con is not None:
                cur.close()
                con.close()

    def obtenerHistorialProfesionesId(self, id):
        """Metodo obtenerHistoriaProfesionesId.
        
        Obtiene el historial de profesiones por id de persona.

        """
        consulta = """
            select
	            array_to_json(array_agg(row_to_json(data))) resultado
            from
	            (
                    select
                        his.hisp_id idhistorial,
                        his.per_id idpersona,
                        his.pro_id idprofesion,
                        pro.pro_des profesion,
                        his.hisp_puesto_laboral puesto_laboral,
                        his.hisp_lugar_trabajo lugar_trabajo
                    from
                        referenciales.historial_profesiones his
                    left join referenciales.profesiones pro on
                        his.pro_id = pro.pro_id
                    where
                        his.per_id = %s  ) data;
        """

        try:
            
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.execute(consulta, (id, ))
            return cur.fetchone()

        except con.Error as e:
            print(e.pgerror)
            return False
        finally:
            if con is not None:
                cur.close()
                con.close()

    def guardarNombreFoto(self, idadi, nombre):
        """Metodo guardarNombreFoto.

        Se define el guardado del nombre de la foto
        en la BD.

        """

        # SQL
        consulta = "UPDATE membresia.admision_adicionales SET add_foto = %s WHERE add_id = %s"
        try:

            conexion = Conexion()
            con = conexion.getConexion()

            cur = con.cursor()

            cur.execute(consulta, (nombre, idadi))

            con.commit()

            return True

        except con.Error as e:

            print(e.pgerror)
            return False

        finally:

            if con is not None:
                cur.close()
                con.close()

    def guardarFormulario(self, idpersona, idnacionalidad, lugarnacimiento, alergias, tiposangre, capacidad_diferente, datos_tabla_nuevos, datos_tabla_eliminar):
        
        # SQL
        consulta1 = """
            UPDATE 
                membresia.admision_adicionales 
            SET 
                nac_id=%s, add_lugarnac=%s, san_id=%s, 
                add_alergias=%s, add_capacdife=%s, creado_por_usuario=null, fecha_modificado = now() 
            WHERE 
                add_id=%s;
        """

        parametros1 = (idnacionalidad, lugarnacimiento, tiposangre,
                       alergias, capacidad_diferente, idpersona, )

        consulta2 = """
            INSERT INTO referenciales.historial_profesiones
            (per_id, pro_id, hisp_puesto_laboral, hisp_lugar_trabajo)
            VALUES(%s, %s, %s, %s);
        """

        consulta3 = """
            DELETE referenciales.historial_profesiones 
            WHERE per_id = %s AND pro_id = %s AND hisp_puesto_laboral = %s AND hisp_lugar_trabajo = %s;
        """
        try:

            conexion = Conexion()
            conexion.autocommit = False
            con = conexion.getConexion()
            cur = con.cursor()

            # Paso 1 : Guardar el admision adicionales
            cur.execute(consulta1, parametros1)

            # Paso 2 : Procesar historial de profesiones.
            # Agregar nuevo historial.
            # Verificar existencia
            if len(datos_tabla_nuevos) != 0:                

                for i in datos_tabla_nuevos:                    
                    
                    cur.execute(consulta2, (idpersona, i['idprofesion'], i['puesto'], i['lugartrabajo'], ))
                
            else:
                print("La lista de nuevos esta vacia ")

            # Eliminar historial            
            if len(datos_tabla_eliminar) != 0:

                for i in datos_tabla_eliminar:
                    
                    cur.execute(consulta3, (idpersona, i['idprofesion'], i['puesto'], i['lugartrabajo'], ))
            else:
                print("La lista de eliminados esta vacia")

            # Commit
            con.commit()

            return True
        except con.Error as e:
            print(e.pgerror)
            return False
        finally:
            if con is not None:
                cur.close()
                con.close()
    
    def eliminarHistorial(self, idpersona, idprofesion, puesto_laboral, lugar_trabajo):
        """Metodo eliminarHistorial.

        Elimina un registro de la tabla historial_profesiones por 
        id de persona.

        """

        # SQL
        consulta = """
            DELETE FROM
                referenciales.historial_profesiones
            WHERE
                per_id = %s AND pro_id = %s AND hisp_puesto_laboral = %s AND hisp_lugar_trabajo = %s;
        """
        parametros = (idpersona, idprofesion, puesto_laboral, lugar_trabajo, )

        try:
            

            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.execute(consulta, parametros)
            con.commit()
            return True

        except con.Error as e:
            
            print(e.pgerror)
            return False

        finally:
            if con is not None:
                cur.close()
                con.close()
