from app.Models.TipoDocumentoModel import TipoDocumentoModel

from app.Models.PersonaModel import PersonaModel

##### Funciones que retornan datos de referenciales ######

def obtenerListaMiembrosDoc():
    pass

def obtenerTipoDocumentos():
    """Función obtenerTipoDocumentos.

    Según la instancia, obtiene una un array de objetos JSON.

    """
    docu = TipoDocumentoModel()

    return docu.listarTodos()

def obtenerPersonas():
    """Función obtenerPersonas.

    Según la instancia, obtiene una un array de objetos JSON.

    """
    p = PersonaModel()

    return p.listarPersonasJSON()
