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
                                     email, postal, idformacontacto, otraiglesia, iglesia, fechacontacto if fechacontacto !='' else None, requierevisita, nuevoenciudad,
                                     fechaultimavisitado if fechaultimavisitado != '' else None, idconyuge if idconyuge != '' else None,  nrohijos if nrohijos !='' else None,))

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
            # pop() elimina un elemento de la lista, es raro recibir NoneType
            telefonos.pop(0)            
            for item in telefonos:
                
                cur.execute(consulta04, (item['tipo'], adp_id, item['numero'], ))
                           
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
