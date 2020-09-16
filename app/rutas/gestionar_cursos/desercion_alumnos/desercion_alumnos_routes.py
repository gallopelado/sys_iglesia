from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from app.rutas.gestionar_cursos.desercion_alumnos.DesercionServices import DesercionServices
deser = Blueprint('desercion_alumnos', __name__, template_folder='templates')

@deser.route('/')
def index():
    return render_template('desercion_alumnos/index.html', titulo='Registrar Deserción de alumnos')

@deser.route('/lista_alumnos')
def listaAlumnos():
    return render_template('desercion_alumnos/lista_alumnos.html', titulo='Lista de alumnos')

@deser.route('/formulario_desercion')
def formularioDesercion():
    return render_template('desercion_alumnos/formulario_desercion.html', titulo='Formulario deserción')

#AJAX
##Obtener lista de cursos
@deser.route('/get_cursos_inscriptos')
def getCursosInscriptos():
    ds = DesercionServices()
    data = ds.getCursosInscriptos()
    return jsonify(data)

##Obtener lista de alumnos segun curso
@deser.route('/get_cursos_inscriptos/<int:cur_id>')
def getListaAlumnoCurso(cur_id):
    ds = DesercionServices()
    data = ds.getListaAlumnos(cur_id)
    return jsonify(data if data else {'estado':False, 'mensaje':'No hay cursos con alumnos'})

##Obtener lista de motivo desercion
@deser.route('/get_motivo_desercion')
def getMotivoDesercion():
    ds = DesercionServices()
    data = ds.getMotivoDesercion()
    return jsonify(data)

@deser.route('/get_curso_maestro', methods=['POST'])
def registrarDesercion():
    obj = {
        'mallaid': request.json['mallaid'], 'curid': request.json['curid'], 'perid': request.json['perid'],
        'mdid': request.json['mdid'], 'alddescripcion': request.json['alddescripcion'], 'aldestado': True,
        'creacionfecha': None, 'creacionusuario': None
    }
    ds = DesercionServices()
    data = ds.registrarDesercion(obj)
    return jsonify(data)