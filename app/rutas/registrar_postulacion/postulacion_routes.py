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
