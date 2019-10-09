# Se importan las librerias basicas
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify

# Registrar Blueprint
candi = Blueprint('registrar_candidatos', __name__, template_folder='templates')

@candi.route('/')
def index_candidados():
    titulo = 'Registrar lista de candidatos por Postulación'
    return render_template('registrar_candidatos/index.html', titulo=titulo)


# Rutas para AJAX
#@candi.route('/traer_postulaciones/<>')