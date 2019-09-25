# Se importan las librerias basicas
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify

# Importar funciones genericas
from app.rutas.registrar_postulacion.helpers import validarFormulario

# Importar modelos
from app.Models.ReferencialModel import ReferencialModel

postu = Blueprint('registrar_postulacion', __name__, template_folder='templates')

@postu.route('/')
def index_postulacion():

    return render_template('registrar_postulacion/index.html')


@postu.route('/frm_postulacion', methods=['GET'])
def frmPostulacion():

    return render_template('registrar_postulacion/formulario_postulacion.html')


# Rutas para AJAX
@postu.route('/guardar_formulario', methods=['PUT'])
def guardarFormulario():

    validarFormulario(request)

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
