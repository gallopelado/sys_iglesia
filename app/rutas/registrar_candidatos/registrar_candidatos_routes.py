# Se importan las librerias basicas
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify

# Se importa el modelo.
from app.Models.ListaCandidatoModel import ListaCandidatoModel

# Registrar Blueprint
candi = Blueprint('registrar_candidatos', __name__, template_folder='templates')

# Generar una instancia del modelo
candim = ListaCandidatoModel()

@candi.route('/')
def index_candidados():
    titulo = 'Registrar lista de candidatos por Postulación'
    return render_template('registrar_candidatos/index.html', titulo=titulo)


@candi.route('/asignar_candidatos/<int:idpostulacion>', methods=['GET'])
def asignarCandidatos(idpostulacion):
    titulo = 'Formulario lista de candidatos'
    return render_template('registrar_candidatos/formulario_candidatos.html', titulo=titulo, idpostulacion=idpostulacion)


# Rutas para AJAX
@candi.route('/traer_postulaciones/<string:opcion>', methods=['GET'])
def traerPostulaciones(opcion):
    lista = candim.traerPostulaciones(opcion)
    return jsonify(lista)