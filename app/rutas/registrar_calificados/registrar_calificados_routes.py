# Se importan las librerias basicas
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify

# Se importa el modelo.
from app.Models.ListaCalificadosModel import ListaCalificadosModel

# Registrar Blueprint
cali = Blueprint('registrar_calificados', __name__, template_folder='templates')

# Generar una instancia del modelo.
calim = ListaCalificadosModel()

titulo = 'Registrar Lista de Calificados'

@cali.route('/')
def index_calificados():
    res = calim.obtenerPostulaciones()    
    return render_template('registrar_calificados/index.html', titulo=titulo, lista=res)


@cali.route('/formulario/<int:idpostulacion>', methods=['GET'])
def revisar(idpostulacion):
    titulo = 'Formulario Evaluación'
    return render_template('registrar_calificados/formulario.html', titulo=titulo, lista=None, detalle=None)