# Se importa la Clase Conexion
from app.Conexion.Conexion import Conexion


class FormAdmisionModel():
    """Clase FormAdmisionModel.

    Se definen los metodos para acceder a la base de datos
    como tambien procesarlos. Esta clase es de movimiento.

    """

    def guardar(self, idpersona, fechanac, direccion, idciudad, idsocial, idfamiliar, fechamatri,
                email, postal, fechacontacto, ecivil, sexo, idformacontacto, otraiglesia, requierevisita, nuevoenciudad,
                idconyuge, iglesia, fechaultimavisitado, nrohijos, familia, lista_padres, telefonos):

        # Inserta en tabla admision_persona y retorna id del recien insertado.
        consulta01 = """
            INSERT INTO membresia.admision_persona
            (adp_id, adp_fechanac, adp_direccion, ciu_id, cls_id, adp_ecivil, adp_sexo, rf_id, fa_id, adp_fechamatri, adp_email, adp_postal, 
            foc_id, adp_otraiglesia, adp_iglesia, adp_fechaprimercontacto, adp_requierevisita, adp_nuevoenciudad, adp_ultimavisita, conyuge_id, 
            adp_nrohijos, 
            adp_estado, adp_ultimamodif)
            VALUES(%s, %s, UPPER(%s), %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, UPPER(%s), %s, %s, %s, %s, %s, %s, true, null)
            RETURNING adp_id;
        """
        # Inserta en tabla padres espirituales.
        consulta02 = """
            INSERT INTO referenciales.padres_espirituales(per_id, padre_id, fecharegistro, estado) VALUES(%s, %s, now(), true);
        """
        # Obtiene el id de persona segun nombre y apellido.
        consulta03 = """
            SELECT per_id FROM referenciales.personas WHERE per_nombres = %s AND per_apellidos = %s;
        """

        # Inserta en tabla telefonos.
        consulta04 = "INSERT INTO referenciales.telefonos_persona(tipo_tel, per_id, telefono)VALUES(%s, %s, %s);"

        # Inserta en formulario_adicionales
        consulta05 = "INSERT INTO membresia.admision_adicionales(add_id, add_estado)VALUES(%s, true);"

        try:

            # Traer la conexion
            conexion = Conexion()
            con = conexion.getConexion()

            # Deshabilitar el autocommit
            conexion.autocommit = False
            cur = con.cursor()

            # Paso 01: Guardar datos del formulario.
            # Insertar en admision_persona
            cur.execute(consulta01, (idpersona, fechanac, direccion, idciudad, idsocial, ecivil, sexo, idfamiliar, familia, fechamatri if fechamatri != '' else None,
                                     email, postal, idformacontacto, otraiglesia, iglesia, fechacontacto if fechacontacto != '' else None, requierevisita, nuevoenciudad,
                                     fechaultimavisitado if fechaultimavisitado != '' else None, idconyuge if idconyuge != '' else None,  nrohijos if nrohijos != '' else None,))

            # El adp_id de la tabla admision_persona
            adp_id = cur.fetchone()[0]

            # Paso 02: Guardar datos de los padres.
            if len(lista_padres) == 0:

                print(f"Lista de padres vacia, {lista_padres}")

            else:

                # print(lista_padres)
                li = []  # [['JUAN JOSE', ' GONZALEZ RAMIREZ'], ['CARMENCITA MARIA', ' LOPEZ'], ['CARLOS', ' RODAS']]
                for persona in lista_padres:
                    li.append(persona.split(","))

                for persona in li:

                    # print(f"Nombres: {persona[0].strip()}, apellidos: {persona[1].strip()}")
                    cur.execute(
                        consulta03, (persona[0].strip(), persona[1].strip(), ))

                    # El bendito ID del ñembo espirituoso
                    id_padre = cur.fetchone()[0]
                    if id_padre:

                        # hacer insercion
                        cur.execute(consulta02, (adp_id, id_padre))

                    else:
                        print('Esta persona no existe en la base de datos')

            # Paso 03: Guardar datos de telefonos
            if len(telefonos) != 0:
            # pop() elimina un elemento de la lista, es raro recibir NoneType
                telefonos.pop(0)
                for item in telefonos:

                    cur.execute(
                        consulta04, (item['tipo'], adp_id, item['numero'], ))
            else:
                print(f"Lista de telefonos vacia = {telefonos}")

           # Paso 04: Inserta nuevo registro del formulario de datos adicionales.
            cur.execute(consulta05, (adp_id,))

           # COMMIT RICOLIN
            con.commit()

            return True

        except con.Error as e:
            print(e.pgerror)
            return e.pgerror
        finally:
            if con is not None:
                cur.close()
                con.close()

    def modificar(self, idadmision, fechanac, direccion, idciudad, idsocial, idfamiliar, fechamatri,
                  email, postal, fechacontacto, ecivil, sexo, idformacontacto, otraiglesia, requierevisita, nuevoenciudad,
                  iglesia, fechaultimavisitado, idconyuge, nrohijos, familia, borrarTel, agregarTel, nuevosPadres, borrarPadres):

        # SQL
        consulta1 = """
        
            UPDATE membresia.admision_persona
            SET adp_fechanac=%s, adp_direccion=UPPER(%s), ciu_id=%s, cls_id=%s, adp_ecivil=%s, adp_sexo=%s, rf_id=%s, fa_id=%s, adp_fechamatri=%s, adp_email=UPPER(%s), adp_postal=%s,
            foc_id=%s, adp_otraiglesia=%s, adp_iglesia=UPPER(%s), adp_fechaprimercontacto=%s, adp_requierevisita=%s,
            adp_nuevoenciudad=%s, adp_ultimavisita=%s, conyuge_id=%s, adp_nrohijos=%s, adp_estado=true, adp_ultimamodif=now()
            WHERE adp_id=%s;

         """
        parametros1 = (fechanac, direccion, idciudad, idsocial, ecivil, sexo, idfamiliar, familia, fechamatri if fechamatri != '' else None,
                       email if email != '' else None, postal if postal != '' else None, idformacontacto, otraiglesia, iglesia,
                       fechacontacto if fechacontacto != '' else None, requierevisita, nuevoenciudad, fechaultimavisitado if fechaultimavisitado != '' else None,
                       idconyuge if idconyuge != '' else None, nrohijos if nrohijos != '' else None, idadmision,)

        consulta2 = """ 
        
            INSERT INTO referenciales.telefonos_persona
            (tipo_tel, per_id, telefono)
            VALUES(%s, %s, %s);
        
        """
        consulta3 = """ 

            DELETE FROM referenciales.telefonos_persona
            WHERE per_id = %s AND telefono= %s;

        """

        consulta4 = """

            INSERT INTO referenciales.padres_espirituales(per_id, padre_id, fecharegistro, estado) VALUES(%s, %s, now(), true);

        """

        # Obtiene el id de persona segun nombre y apellido.
        consulta5 = """
            SELECT per_id FROM referenciales.personas WHERE per_nombres = %s AND per_apellidos = %s;
        """

        consulta6 = """ 
        
            DELETE FROM referenciales.padres_espirituales
            WHERE per_id=%s AND padre_id=%s;

        
        """
        try:
            conexion = Conexion()
            conexion.autocommit = False
            con = conexion.getConexion()
            cur = con.cursor()

            # Paso 01: Hacer actualizacion en admision_persona.
            cur.execute(consulta1, parametros1)

            # Paso 02: Agregado de registros, padres y telefonos.
            # Telefonos
            if len(agregarTel) != 0:

                for tel in agregarTel:
                    #pass
                    # Insert a telefono
                    cur.execute(consulta2, (tel['tipo'], idadmision, tel['numero'],))
            else:

                print(f"Lista de telefonos vacia = {agregarTel}")

            if len(borrarTel) != 0:

                for tel in borrarTel:
                    #pass
                    # print(tel)
                    cur.execute(consulta3, (idadmision, tel['numero']))
            else:
                print(f"Lista de telefonos vacia = {borrarTel}")

            # Padres espirituales
            if len(nuevosPadres) != 0:
                for p in nuevosPadres:

                    # Separa nombre y apellido en una lista.
                    persona = p['persona'].split(',')
                    # Extraer nombre y apellido.
                    nombres = persona[0].strip()
                    apellidos = persona[1].strip()
                    cur.execute(consulta5, (nombres, apellidos, ))
                    idpadre = cur.fetchone()[0]
                    cur.execute(consulta4, (idadmision, idpadre))
            else:
                print(f"Lista de nuevosPadres vacia = {nuevosPadres}")

            if len(borrarPadres) != 0:
                for p in borrarPadres:
                    #print(p)
                    cur.execute(consulta6, (idadmision, p['idpadre']))
            else:
                print(f"Lista de borrarPadres vacia = {borrarPadres}")
            
            # Suculento commit
            con.commit()

            return True
        except con.Error as e:

            print(e.pgerror)
            return False

        finally:
            if con is not None:
                cur.close()
                con.close()

        # Paso 02:

    def listar_formularios(self):

        # Consulta SQL
        consulta = """

            SELECT 
            adp.adp_id, per.per_nombres||' '||per.per_apellidos as persona, per.per_ci as cedula,
            (select to_char(adp.adp_fecharegistro, 'YYYY/MM/DD'::TEXT) as fechaingreso)
            FROM membresia.admision_persona adp join referenciales.personas per on adp.adp_id=per.per_id
            WHERE adp_estado=true;
        
        """

        try:
            conexion = Conexion()
            con = conexion.getConexion()

            cur = con.cursor()
            cur.execute(consulta)

            lista = cur.fetchall()

            # print(lista)

            return lista

        except con.Error as e:

            print(e.pgerror)
            return e.pgerror

        finally:
            if con is not None:
                cur.close()
                con.close()

    def obtenerDatosModal(self, idadmision):

        # SQL
        consulta = """ 
        
            SELECT ad.adp_id, pe. per_nombres ||' '|| pe.per_apellidos as personas
            FROM membresia.admision_persona ad JOIN referenciales.personas pe ON ad.adp_id = pe.per_id
            WHERE ad.adp_id = %s;
        
        """
        try:

            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()

            cur.execute(consulta, (idadmision,))

            encontrado = cur.fetchone()

            return encontrado

        except con.Error as e:

            print(e.pgerror)

            return False

        finally:
            if con is not None:
                cur.close()
                con.close()

    def baja(self, idadmision, razonbaja, obs):
        """Metodo baja.

        Se encarga de actualizar las tablar formulario de admision y persona.

        """

        # Consulta SQL

        sp = "membresia.baja_admision"
        parametros = (idadmision, razonbaja, obs, )

        try:

            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()

            # callproc ejecuta el procedimiento.
            cur.callproc(sp, parametros)

            con.commit()

            return True

        except con.Error as e:

            print(e.pgerror)
            return False

        finally:

            if con is not None:
                cur.close()
                con.close()

    def obtenerDatosFormularioId(self, idadmision):

        # SQL
        consulta = """ 
        
           SELECT adp.adp_id idadmision, adp.adp_fechanac::varchar fechanacimiento, adp.adp_direccion direccion, 
            adp.ciu_id, adp.cls_id, adp.adp_ecivil estado_civil, adp.adp_sexo sexo, adp.rf_id, adp.fa_id,
            adp.adp_fechamatri::varchar fecha_de_matrimonio, adp.adp_email email, adp.adp_postal postal, 
            adp.foc_id, adp.adp_otraiglesia, adp.adp_iglesia iglesia, adp.adp_fechaprimercontacto::varchar fecha_primer_contacto,
            adp.adp_requierevisita requiere_visita, adp.adp_nuevoenciudad nuevo_en_ciudad, 
            adp.adp_ultimavisita::varchar ultimavisita, adp.conyuge_id, adp.adp_nrohijos nro_hijos,
            pe.per_nombres||' '||pe.per_apellidos persona
            FROM membresia.admision_persona adp
            INNER JOIN referenciales.personas pe ON adp.adp_id = pe.per_id
            WHERE adp.adp_id = %s;

        """

        try:

            conexion = Conexion()
            con = conexion.getConexion()

            cur = con.cursor()
            cur.execute(consulta, (idadmision,))

            datos = cur.fetchone()

            # print(datos)
            return datos

        except con.Error as e:

            print(e.pgerror)
            return False

        finally:
            if con is not None:
                cur.close()
                con.close()

    def obtenerTelefonos(self, idadmision):

        # SQL
        consulta = """ 
        
            SELECT tel_id, tipo_tel, per_id, telefono
            FROM referenciales.telefonos_persona
            WHERE per_id = %s;

        """

        try:

            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()

            cur.execute(consulta, (idadmision, ))

            data = cur.fetchall()

            return data

        except con.Error as e:
            print(e.pgerror)
            return False
        finally:
            if con is not None:
                cur.close()
                con.close()

    def obtenerPadres(self, idadmision):

        # SQL
        consulta = """ 
        
            SELECT  
            pes.padre_id, p.per_nombres||', '||p.per_apellidos persona
            FROM referenciales.padres_espirituales pes
            INNER JOIN referenciales.personas p ON pes.padre_id = p.per_id
            WHERE pes.per_id = %s;

        """

        try:

            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()

            cur.execute(consulta, (idadmision, ))

            data = cur.fetchall()

            return data

        except con.Error as e:
            print(e.pgerror)
            return False
        finally:
            if con is not None:
                cur.close()
                con.close()

    def getAdmisionesActivas(self, estado):
        # SQL
        procedimiento = 'membresia.get_miembro_admision_json'
        try:
            
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.callproc(procedimiento, (estado, ))
            return cur.fetchall()

        except con.Error as e:
            print(str(e.pgerror).encode('utf-8'))
            return False
        finally:
            if con is not None:
                cur.close()
                con.close()
