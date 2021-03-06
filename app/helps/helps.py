import os,time
from werkzeug.utils import secure_filename
from app.Conexion.Conexion import Conexion

def limpiar_campo(palabra):
    """Funcion limpiar_campo.

    Limpiar campo de espacios a la derecha e izquierda.

    """
    palabra = palabra.strip()
    palabra = palabra.lstrip()
    return palabra

def verificaNull(campo):
    if campo != '' and campo != 'null':
        return campo
    else:
        return None

def guardarDocumento(peticion, clave, app, claveconfig):

    if peticion.files:

        # Verificar si existe el fichero.
        #listaDocu = os.listdir(app.config[claveconfig])

        # Recuperar de la peticion.
        documento = peticion.files[clave]
        nombreDocumento = secure_filename(documento.filename)        
        
        # if listaDocu:
        #     for item in listaDocu:
        #         if item == nombreDocumento:
        #             # Elimina primer fichero.
        #             os.remove(os.path.join(
        #                 app.config[claveconfig], nombreDocumento))
        #             # Guardar en el directorio.
        #             documento.save(os.path.join(
        #                 app.config[claveconfig], nombreDocumento))
                    
        #         else:               
        #             # Guardar en el directorio.
        #             documento.save(os.path.join(
        #                 app.config[claveconfig], nombreDocumento))
        # else:
            # Guardar en el directorio.
        documento.save(os.path.join(app.config[claveconfig], nombreDocumento))

    return False            

def fechaActual():
    '''fechaActual.
    Retorna la fecha del sistema.
    '''
    localtime = time.localtime(time.time())
    fecha_actual = f'{localtime.tm_mday}-{localtime.tm_mon}-{localtime.tm_year}'
    return fecha_actual

def fechaFormatoLargo(fecha):
    '''fechaFormatoLargo.
    Retorna la fecha en formato largo.
    '''
    try:
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        cur.callproc('public.fecha_formatolargo', (fecha,))
        return cur.fetchone()[0]        
    except con.Error as e:
        print(e.pgerror)
    finally:
        if con is not None:
            cur.close()
            con.close()