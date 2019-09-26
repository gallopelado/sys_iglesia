
def validarFormulario(req):
    '''Funcion validarFormulario.

    Esta funcion permite validar todos los datos del formulario,
    excepto el binario o documento.

    '''

    # Variables de entrada.
    datos = req.form
    idcomite = datos['idcomite']
    descripcion = datos['descripcion']
    idpuestos = datos['idpuestos']
    vacancias = datos['vacancias']
    fechainicio = datos['fechainicio']
    fechafin = datos['fechafin']    

    # Limpiar espacios en blanco.
    idcomite = idcomite.strip()
    descripcion = descripcion.strip()
    idpuestos = idpuestos.strip()
    vacancias = vacancias.strip()
    fechainicio = fechainicio.strip()
    fechafin = fechafin.strip()

    # Si alguno esta vacío, retorna False.
    if not idcomite and not descripcion and not idpuestos and not vacancias and not fechainicio and not fechafin:
        return False

    return True


EXTENSIONES_PERMITIDAS = {'pdf', 'epub'}


def permitido_file(filename):
    return '.' in filename and filename.split('.', 1)[1].lower() in EXTENSIONES_PERMITIDAS


def validarDocumento(req):

    if 'docu_binario' not in req.files:
        return None

    return True
