# Se importan las librerias basicas
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
# Importar modelos

# Registrar modulo
# gcr - generar contrato reserva
gcr = Blueprint('contrato_reserva', __name__, template_folder='templates')
titulo = 'Generar contrato por reserva'

@gcr.route('/')
def index_contrato():
    return render_template('contrato_reserva/index.html', titulo=titulo)


@gcr.route('/formulario_contrato')
def formularioContrato():
    titulo = 'Formulario contrato'
    return render_template('contrato_reserva/formulario.html', titulo=titulo)