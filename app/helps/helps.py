import os
from werkzeug.utils import secure_filename

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

def recuperaDocumento():
    """Funcion recuperaDocumento.

    Recupera ruta del fichero guardado.

    """
    pass
