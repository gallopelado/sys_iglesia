def validarFormulario(req):
    '''Funcion validarFormulario.

    Esta funcion permite validar todos los datos del formulario,
    excepto el binario o documento.

    '''

    print('Desde la funcion validarFormulario')
    print(f'Recibido {req.form}')

    # Variables de entrada.
    datos = req.form;
    idcomite = datos['idcomite']
    descripcion = datos['descripcion']
    idpuestos = datos['idpuestos']
    vacancias = datos['vacancias']
    fechainicio = datos['fechainicio']
    fechafin = datos['fechafin']
