# Se importan las librerias basicas
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify

# Se importa el modelo.
from app.Models.ListaCandidatoModel import ListaCandidatoModel
from app.Models.MiembroPerfilModel import MiembroPerfilModel

# Registrar Blueprint
candi = Blueprint('registrar_candidatos', __name__, template_folder='templates')

# Generar una instancia del modelo
candim = ListaCandidatoModel()

@candi.route('/')
def index_candidatos():
    titulo = 'Registrar lista de candidatos por Postulación'
    return render_template('registrar_candidatos/index.html', titulo=titulo)


@candi.route('/asignar_candidatos/<int:idpostulacion>', methods=['GET'])
def asignarCandidatos(idpostulacion):
    editar = True
    titulo = 'Formulario lista de candidatos'
    lista = candim.traerListaCandidatos(idpostulacion)
    detalle = lista[4] if len(lista[4])>0 else None        
    return render_template('registrar_candidatos/formulario_candidatos.html', titulo=titulo, idpostulacion=idpostulacion, lista=lista, detalle=detalle, editar=editar)


@candi.route('/ver_candidatos/<int:idpostulacion>', methods=['GET'])
def verCandidatos(idpostulacion):
    ver = True
    titulo = 'Ver lista de candidatos'
    lista = candim.traerListaCandidatos(idpostulacion)
    detalle = lista[4] if len(lista[4])>0 else None        
    return render_template('registrar_candidatos/formulario_candidatos.html', titulo=titulo, idpostulacion=idpostulacion, lista=lista, detalle=detalle, ver=ver)

# Rutas para AJAX
@candi.route('/traer_postulaciones/<string:opcion>', methods=['GET'])
def traerPostulaciones(opcion):
    lista = candim.traerPostulaciones(opcion)
    return jsonify(lista)


@candi.route('/traer_detalle_candidatos/<string:idpostulacion>')
def traerDetalleCandidatos(idpostulacion):
    detalle = candim.traerDetalleCandidatos(idpostulacion)
    return jsonify(detalle)

@candi.route('/traer_candidatos')
def traerCandidatos():

    perf = MiembroPerfilModel()
    lista = perf.traerCandidatos()
    return jsonify(lista)


@candi.route('/eliminar_candidato', methods=['PUT'])
def eliminarCandidato():
    print(request.json)

    return jsonify({'procesando':True})