# Se importan las librerias basicas
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
# Importar modelos
from app.Models.actividad_models.ActividadAnualModel import ActividadAnualModel
# Registrar módulo
# acan -- actividad anual
acan = Blueprint('actividades_anuales', __name__, template_folder='templates')
titulo = 'Registrar actividades anuales de la organización'
# Instancias
actim = ActividadAnualModel()
@acan.route('/')
def index_acti_anuales():
    lista = actim.obtenerAnho()
    return render_template('registrar_actividades_anuales/index.html', titulo=titulo, anhos=lista)