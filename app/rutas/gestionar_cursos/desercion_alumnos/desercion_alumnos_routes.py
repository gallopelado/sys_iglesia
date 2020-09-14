from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from app.rutas.gestionar_cursos.desercion_alumnos.DesercionServices import DesercionServices
deser = Blueprint('desercion_alumnos', __name__, template_folder='templates')

@deser.route('/')
def index():
    return render_template('desercion_alumnos/index.html', titulo='Registrar Deserción de alumnos')

#AJAX
##Obtener maestros
@deser.route('/get_maestros')
def getMaestros():
    ds = DesercionServices()
    data = ds.getMaestros()
    return jsonify(data)

##Obtener lista de cursos segun maestro y turno
@deser.route('/get_curso_maestro/<int:perid>/<string:turno>')
def getCursoMaestro(perid, turno):
    ds = DesercionServices()
    data = ds.getCursoMaestro(perid, turno)
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