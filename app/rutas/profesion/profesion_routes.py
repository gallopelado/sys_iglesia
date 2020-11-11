# Se importan las librerias basicas.
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, session, abort

# Se importa el modelo.
from app.Models.ProfesionModel import ProfesionModel

profesion = Blueprint('profesion', __name__, template_folder='templates')

@profesion.before_request
def before_request():
    if 'username' not in session:
        return redirect(url_for('login.login'))
    elif 'grupo' not in session:
        return redirect(url_for('login.login'))
    elif 'username' in session and 'grupo' in session and session['grupo']!='ADMIN':
        abort(403, description="Acceso prohibido")

@profesion.route('/')
def index_profesion():
    return "Index de Profesion"

# Para AJAX.
@profesion.route('/listar_profesiones', methods=['GET'])
def listar_profesiones():

    prof = ProfesionModel()

    return jsonify(prof.listarTodos())

@profesion.route('/guardar', methods=['POST'])
def guardar():

    # Recuperar valores del formulario.
    operacion = request.form['op']
    descripcion = request.form['descripcion']

    prof = ProfesionModel()
    res = prof.guardar(operacion, None, descripcion)

    if res == True:
        return jsonify({"guardado": True})
    else:
        return jsonify({"guardado": False})