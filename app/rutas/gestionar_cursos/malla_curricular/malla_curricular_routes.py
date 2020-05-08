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

# Ajax
@mc.route('/mallas')
def mallasCurriculares():
    ms = MallaCurricularServices()
    lista = ms.obtenerTodasMallasCurriculares()
    return jsonify(lista)