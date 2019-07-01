# Se importan las librerias basicas.
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify

# Se importa el modelo.
from app.Models.ProfesionModel import ProfesionModel

profesion = Blueprint('profesion', __name__, template_folder='templates')

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