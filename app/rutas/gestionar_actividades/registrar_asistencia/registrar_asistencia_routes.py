# Se importan las librerias basicas
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
# Importar modelos

# Registrar modulo
asis = Blueprint('registrar_asistencia', __name__, template_folder='templates')
titulo = 'Registrar asistencias de miembros de la iglesia'

@asis.route('/')
def index_asistencia():
    return render_template('registrar_asistencia/index.html', titulo=titulo)


@asis.route('/formulario_asistencia')
def formularioAsistencia():
    return render_template('registrar_asistencia/formulario.html', titulo='Formulario Asistencia')