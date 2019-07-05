from app.Models.TipoDocumentoModel import TipoDocumentoModel

##### Funciones que retornan datos de referenciales ######

def obtenerTipoDocumentos():
    """Función obtenerTipoDocumentos.

    Según la instancia, obtiene una un array de objetos JSON.

    """
    docu = TipoDocumentoModel()

    return docu.listarTodos()
