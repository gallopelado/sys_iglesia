#import json
# Librerias basicas
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, json
from werkzeug.wrappers import Response

from app.rutas.gestionar_cursos.malla_curricular.MallaCurricularServices import MallaCurricularServices

mc = Blueprint('malla_curricular', __name__, template_folder='templates')

@mc.route('/')
def index():

    return render_template('malla_curricular/index.html', titulo='Registrar Malla Curricular')

    #return Response(json.dumps(lista), mimetype='application/json')
    #return jsonify(lista)

@mc.route('/form_malla_curricular')
def formMallaCurricular():
    ms = MallaCurricularServices()
    res = ms.verificarAnhoHabil()
    if res:
        flash('Lo siento, el año actual esta en uso', 'warning')
        return redirect(url_for('malla_curricular.index'))
    return render_template('malla_curricular/form_malla_curricular.html', titulo='Formulario Malla Curricular')

@mc.route('/form_malla_curricular/<int:idmalla>')
def formMallaCurricular_editar(idmalla):
    return render_template('malla_curricular/form_malla_curricular.html', titulo='Formulario Malla Curricular', idmalla=idmalla)

# Ajax
@mc.route('/mallas')
def mallasCurriculares():
    ms = MallaCurricularServices()
    lista = ms.obtenerTodasMallasCurriculares()
    return jsonify(lista)

@mc.route('/get_areas')
def getAreas():
    ms = MallaCurricularServices()
    lista = ms.obtenerTodasAreas()
    return jsonify(lista)

@mc.route('/get_cursos')
def getCursos():
    ms = MallaCurricularServices()
    lista = ms.obtenerTodasCursos()
    return jsonify(lista)

@mc.route('/get_areacursos/<int:idarea>')
def getAreaCursos(idarea):
    ms = MallaCurricularServices()
    lista = ms.obtenerAreaCursosAreaId(idarea)
    return jsonify(lista)

@mc.route('/get_anhohabil')
def getAnhoHabil():
    ms = MallaCurricularServices()
    objeto = ms.obtenerAnhoHabil()
    return jsonify(objeto)

@mc.route('/get_cursosregistrados/<int:idmalla>')
def getCursosRegistrados(idmalla):
    ms = MallaCurricularServices()
    lista = ms.obtenerCursosRegistrados(idmalla)
    return jsonify(lista)

@mc.route('/guardar', methods=['POST'])
def guardar():
    anho_id = request.json['anho_id']
    cur_id = request.json['cur_id']
    ms = MallaCurricularServices()
    res = ms.guardar(anho_id, cur_id, True)
    return jsonify({"estado":res})

@mc.route('/agregar_nuevos_cursos_malla', methods=['PUT'])
def agregarNuevosCursosMalla():
    malla_id = request.json['malla_id']
    cur_id = request.json['cur_id']
    estado = request.json['estado']
    ms = MallaCurricularServices()
    res = ms.agregarNuevosCursosMalla(malla_id, cur_id, estado)
    return jsonify({"estado":res})

@mc.route('/anular_curso_malla', methods=['PUT'])
def anularCursoMalla():
    malla_id = request.json['malla_id']
    cur_id = request.json['cur_id']
    estado = request.json['estado']
    ms = MallaCurricularServices()
    res = ms.anularCursoMalla(malla_id, cur_id, estado)
    return jsonify({"estado":res})



