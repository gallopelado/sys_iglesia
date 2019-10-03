# Se importan las librerias basicas
import os
from flask import current_app as app, Blueprint, render_template, request, redirect, url_for, flash, jsonify
from werkzeug.utils import secure_filename

# Importar funciones genericas
from app.rutas.registrar_postulacion.helpers import validarFormulario, validarDocumento, permitido_file

# Importar modelos
from app.Models.PostulacionModel import PostulacionModel
from app.Models.ReferencialModel import ReferencialModel

postu = Blueprint('registrar_postulacion', __name__, template_folder='templates')

@postu.route('/')
def index_postulacion():

    p = PostulacionModel()
    lista = p.traerPostulaciones()
    return render_template('registrar_postulacion/index.html', lista = lista)


@postu.route('/frm_postulacion', methods=['GET'])
def frmPostulacion():
    
    return render_template('registrar_postulacion/formulario_postulacion.html')


@postu.route('/frm_postulacion/<int:idpostulacion>', methods=['GET'])
def mostrarFormulario(idpostulacion):
    
    p = PostulacionModel()
    datos_cab = p.traerPostulacionId(idpostulacion)
    datos_det = datos_cab[7]    
    return render_template('registrar_postulacion/formulario_postulacion.html', datos_cab = datos_cab, datos_det = datos_det)


@postu.route('/reprogramar', methods=['PUT'])
def reprogramar():

    # Recolectar datos del cliente.
    opcion = request.json['opcion']
    idpostu = request.json['idpostu']
    fechainicio = request.json['fechainicio']
    fechafin = request.json['fechafin']

    # Validar en caso de opción incorrecta.
    if not opcion:
        return jsonify({ 'estado': False, 'error': 'La opción esta vacía!!' })

    if not idpostu:
        return jsonify({ 'estado': False, 'error': 'No se envió idpostulacion !!' })
    
    # Genera una instancia del modelo.
    pos = PostulacionModel()    

    if opcion == 'dia':
        # Enviando datos al modelo.
        res = pos.reprogramar(opcion, idpostu)
        if res == True:
            return jsonify({'estado': res, 'mensaje': 'Se adelantó 1 día'})
        return jsonify({'estado': False, 'error': res})
    
    elif opcion == 'semana':
        # Enviando datos al modelo.
        res = pos.reprogramar(opcion, idpostu)
        if res == True:
            return jsonify({'estado': res, 'mensaje': 'Se adelantó 1 semana'})
        return jsonify({'estado': False, 'error': res})
    
    elif opcion == 'mes':
        # Enviando datos al modelo.
        res = pos.reprogramar(opcion, idpostu)
        if res == True:
            return jsonify({'estado': res, 'mensaje': 'Se adelantó 1 mes'})
        return jsonify({'estado': False, 'error': res})

    elif opcion == 'personalizado':
        # Verificando si no estan vacías las fechas.
        if not fechainicio:
            return jsonify({'estado': False, 'error': 'La fecha de inicio esta vacía'})
        if not fechafin:
            return jsonify({'estado': False, 'error': 'La fecha de finalización esta vacía'})

        # Enviando datos al modelo.
        res = pos.reprogramar(opcion, idpostu, fechainicio, fechafin)
        if res == True:
            return jsonify({'estado': res, 'mensaje': 'Se reprogramó correctamente'})
        return jsonify({'estado': False, 'error': res})

    else:
        return jsonify({'estado':False, 'error': 'Ninguna opción es válida'})
    

# Rutas para AJAX
@postu.route('/guardar_formulario', methods=['PUT'])
def guardarFormulario():

    postu = PostulacionModel()  
    if validarFormulario(request):
        # Enviar al modelo.
        # Si la persistencia fue un exito, retorna
        # el nombre del documento.
              
        if validarDocumento(request):
            
            # Obtener binario.
            archivo = request.files['docu_binario']
            nombreArchivo = archivo.filename
            
            # validar nombre vacio.
            if nombreArchivo == '':
                nombreArchivo = None

            # validar extension.
            if archivo and permitido_file(archivo.filename):
                # Valida nombre del archivo.
                nombreArchivo = secure_filename(archivo.filename)
            
            # Guardar el nombre en la bd con todo el registro.
            nuevoNombre = postu.guardarNuevaPostulacion(request.form['idcomite'], request.form['descripcion'], nombreArchivo, True, request.form['fechainicio'], request.form['fechafin'], None, request.form['idpuestos'], request.form['vacancias']
                                                        )

            if nuevoNombre or nuevoNombre is not None:
                # Guardar el binario en el sistema.
                archivo.save(os.path.join(app.config['DOCUMENTOS_POSTULACION'], nuevoNombre))        
        else:            
            nombreArchivo = None
            postu.guardarNuevaPostulacion(request.form['idcomite'], request.form['descripcion'], nombreArchivo, True, request.form['fechainicio'], request.form['fechafin'], None, request.form['idpuestos'], request.form['vacancias'])    
    
    flash('Se ha guardado exitosamente la postulacion')
    return jsonify({'procesado': True})


@postu.route('/get_ministerios', methods=['GET'])
def getMinisterios():

    ref = ReferencialModel()
    lista = ref.getReferencialJson('referenciales.ministerios')
    
    return jsonify(lista)


@postu.route('/get_profesiones', methods=['GET'])
def getProfesiones():
    ref = ReferencialModel()
    lista = ref.getReferencialJson('referenciales.profesiones')
    
    return jsonify(lista)
